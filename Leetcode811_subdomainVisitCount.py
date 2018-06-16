# Leetcode811_subdomainVisitCount.py

import collections
def subdomainVisits(cpdomains):
    ans = collections.Counter()
    for domain in cpdomains:
        count, domain = domain.split()
        # print(count, domain)
        count = int(count)
        fragments = domain.split('.')
        # print(fragments)
        for i in range(len(fragments)):
            # print(ans['.'.join(fragments[i:])])
            ans['.'.join(fragments[i:])] += count
    return ['{} {}'.format(cnt, dom) for dom, cnt in ans.items()]
    

print(subdomainVisits(["9001 discuss.leetcode.com", '1000 google.com']))