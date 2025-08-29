pub fn number_of_subarrays(nums: Vec<i32>, k: i32) -> i32 {
    let mut lp = 0;
    let mut odd_count = 0;
    let mut even_count = 0;
    let mut result = 0;

    for rp in 0..nums.len() {
        if nums[rp] % 2 != 0 {
            odd_count += 1;
            even_count = 0;
        }

        while odd_count == k {
            if nums[lp] % 2 != 0 {
                odd_count -= 1;
            }
            lp += 1;
            even_count += 1;
        }

        result += even_count;
    }

    result
}

#[test]
fn test_one() {
    let result = number_of_subarrays(vec![1, 1, 2, 1, 1], 3);

    assert_eq!(result, 2);
}

#[test]
fn test_two() {
    let result = number_of_subarrays(vec![2, 4, 6], 1);

    assert_eq!(result, 0);
}

#[test]
fn test_three() {
    let result = number_of_subarrays(vec![2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2);

    assert_eq!(result, 16)
}
