use std::collections::VecDeque;

struct HitCounter {
    window: VecDeque<i32>,
    curr_time: i32,
}

impl HitCounter {
    fn new() -> Self {
        Self {
            window: VecDeque::new(),
            curr_time: 0,
        }
    }

    fn hit(&mut self, timestamp: i32) {
        self.window.push_back(timestamp);
        self.curr_time = timestamp;
    }

    fn get_hits(&mut self, timestamp: i32) -> i32 {
        self.curr_time = timestamp;

        self.window.retain(|&t| t > timestamp - 300);
        self.window.len() as i32
    }
}
