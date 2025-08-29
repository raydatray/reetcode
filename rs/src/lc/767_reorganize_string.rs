use std::collections::HashMap;

fn reorganize_string(s: String) -> String {
    let n = s.chars().count();
    if n <= 1 {
        return s.to_string();
    }

    let mut counts = s.chars().fold(HashMap::new(), |mut m, c| {
        *m.entry(c).or_insert(0) += 1;
        m
    });

    let (max_count, letter) = counts
        .iter()
        .fold((0usize, '\0'), |(max_c, max_ch), (&ch, &cnt)| {
            if cnt >= max_c {
                (cnt, ch)
            } else {
                (max_c, max_ch)
            }
        });

    if max_count > (n + 1) / 2 {
        return String::new();
    }

    let mut res = std::iter::repeat(' ').take(n).collect::<Vec<_>>();
    let mut idx = 0usize;

    let cnt = counts.get_mut(&letter).unwrap();
    while *cnt > 0 {
        res[idx] = letter;
        idx += 2;
        *cnt -= 1;
    }

    for (ch, mut cnt) in counts.into_iter() {
        while cnt > 0 {
            if idx >= n {
                idx = 1;
            }
            res[idx] = ch;
            idx += 2;
            cnt -= 1;
        }
    }

    res.into_iter().collect()
}

#[test]
fn test_one() {
    let result = reorganize_string(String::from("aab"));
    assert_eq!(result, "aba")
}

#[test]
fn test_two() {
    let result = reorganize_string(String::from("aaab"));
    assert_eq!(result, "");
}
