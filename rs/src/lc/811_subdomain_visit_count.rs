use std::collections::HashMap;

fn subdomain_visit_count(cpdomains: Vec<&str>) -> Vec<String> {
    cpdomains
        .iter()
        .fold(HashMap::new(), |mut map, cpdomain| {
            let (count, domain) = cpdomain.split_once(' ').unwrap();
            let count = count.parse::<usize>().unwrap();
            let parts = domain.split('.').collect::<Vec<_>>();

            for i in 0..parts.len() {
                let subdomain = parts[i..].join(".");
                *map.entry(subdomain).or_insert(0) += count;
            }

            map
        })
        .into_iter()
        .map(|(k, v)| format!("{} {}", v, k))
        .collect()
}

#[test]
fn test_one() {
    let mut result = subdomain_visit_count(vec!["9001 discuss.leetcode.com"]);

    assert_eq!(
        result.sort(),
        vec!["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"].sort()
    );
}

#[test]
fn test_two() {
    let mut result = subdomain_visit_count(vec![
        "900 google.mail.com",
        "50 yahoo.com",
        "1 intel.mail.com",
        "5 wiki.org",
    ]);

    assert_eq!(
        result.sort(),
        vec![
            "900 google.mail.com",
            "50 yahoo.com",
            "1 intel.mail.com",
            "5 wiki.org",
            "5 org",
            "1 mail.com"
        ]
        .sort()
    );
}
