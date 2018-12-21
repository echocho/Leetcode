
def numUniqueEmails(emails):
    """
    :type emails: List[str]
    :rtype: int
    """
    if not emails:
        return 0
    counter = set()
    for i in emails:
        domain = i.split('@')[1]
        local = i.split('@')[0]
        local = local.split('+')[0]
        local = local.replace('.', '')
        counter.add(local+domain)
    return len(counter)

print(numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))

        
