use std::{
    cmp::min,
    collections::HashMap,
    hash::Hash,
    time::{SystemTime, UNIX_EPOCH},
};

#[allow(dead_code)]
struct KVStore<K, V> {
    store: HashMap<K, V>,
    put_buckets: Vec<usize>,
    get_buckets: Vec<usize>,
    last_update: u64,
    metric_window: usize,
}

#[allow(dead_code)]
impl<K, V> KVStore<K, V>
where
    K: Eq + Hash,
    V: Clone
{
    pub fn new(metric_window: usize) -> Self {
        Self {
            store: HashMap::new(),
            put_buckets: vec![0; metric_window],
            get_buckets: vec![0; metric_window],
            last_update: SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_secs(),
            metric_window: metric_window,
        }
    }

    pub fn put(&mut self, key: K, val: V) {
        let now = Self::now();
        self.update_buckets(now);

        let bucket_idx = self.get_bucket_index(now);
        self.put_buckets[bucket_idx] += 1;

        self.store.insert(key, val);
    }

    pub fn get(&mut self, key: K) -> Option<V> {
        let now = Self::now();
        self.update_buckets(now);

        let bucket_idx = self.get_bucket_index(now);
        self.get_buckets[bucket_idx] += 1;

        self.store.get(&key).cloned()
    }

    pub fn put_qps(&mut self) -> f64 {
        let now = Self::now();
        self.update_buckets(now);

        return self.put_buckets.iter().sum::<usize>() as f64 / self.metric_window as f64
    }

    pub fn get_qps(&mut self) -> f64 {
        let now = Self::now();
        self.update_buckets(now);

        return self.get_buckets.iter().sum::<usize>() as f64 / self.metric_window as f64
    }

    fn now() -> u64{
        SystemTime::now().duration_since(UNIX_EPOCH).unwrap().as_secs()
    }

    fn get_bucket_index(&self, now: u64) -> usize {
        return (now % self.metric_window as u64) as usize
    }

    fn update_buckets(&mut self, now: u64) {
        let elapsed = now - self.last_update;

        if elapsed >= self.metric_window as u64 {
            self.put_buckets.fill(0);
            self.get_buckets.fill(0);
        } else {
            let time_diff = now - self.last_update as u64;

            for i in 0..min(time_diff, self.metric_window as u64) {
                let bucket_to_clear = ((self.last_update + i + 1) % self.metric_window as u64) as usize;

                self.put_buckets[bucket_to_clear] = 0;
                self.get_buckets[bucket_to_clear] = 0;
            }
        }

        self.last_update = now;
    }
}
