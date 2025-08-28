"""
https://leetcode.com/problems/accounts-merge/?envType=company&envId=roblox&favoriteSlug=roblox-all

Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.
Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts.
Note that even if two accounts have the same name, they may belong to different people as people could have the same name.
A person can have any number of accounts initially, but all of their accounts definitely have the same name.
After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:
Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

Example 2:
Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]


Constraints:
1 <= accounts.length <= 1000
2 <= accounts[i].length <= 10
1 <= accounts[i][j].length <= 30
accounts[i][0] consists of English letters.
accounts[i][j] (for j > 0) is a valid email.
"""

from typing import Dict, List


class Solution:
    def accounts_merge(self, accounts: List[List[str]]) -> List[List[str]]:
        visited_emails = set()
        adjacent: Dict[str, List[str]] = {}

        def _dfs(merged_accounts: List, email: str):
            visited_emails.add(email)
            merged_accounts.append(email)

            if email not in adjacent.keys():
                return

            for neighbor in adjacent[email]:
                if neighbor not in visited_emails:
                    _dfs(merged_accounts, neighbor)

        for account in accounts:
            first_email = account[1]

            for j in range(2, len(account)):
                account_email = account[j]

                if first_email not in adjacent.keys():
                    adjacent[first_email] = []

                adjacent[first_email].append(account_email)

                if account_email not in adjacent.keys():
                    adjacent[account_email] = []

                adjacent[account_email].append(first_email)

        result = []
        for account in accounts:
            account_name = account[0]
            account_first_email = account[1]

            if account_first_email not in visited_emails:
                merged_account = []
                merged_account.append(account_name)

                _dfs(merged_account, account_first_email)
                merged_account[1:] = sorted(merged_account[1:])
                result.append(merged_account)

        return result


def test_one():
    solution = Solution()
    result = solution.accounts_merge(
        [
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"],
        ]
    )

    assert sorted(result, key=lambda x: x[0]) == sorted(
        [
            ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"],
        ],
        key=lambda x: x[0],
    )


def test_two():
    solution = Solution()
    result = solution.accounts_merge(
        [
            ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
            ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
            ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
            ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
            ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"],
        ]
    )

    assert sorted(result, key=lambda x: x[0]) == sorted(
        [
            ["Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"],
            ["Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"],
            ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"],
            ["Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"],
            ["Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co"],
        ],
        key=lambda x: x[0],
    )
