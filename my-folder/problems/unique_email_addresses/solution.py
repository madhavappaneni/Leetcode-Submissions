class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        validEmails = set()
        
        def emailValidator(email):
            name, domain = email.split('@')
            name = name.split('+')[0].replace('.', '')
            email = name + '@' + domain
            return email
            
        count = 0
        for email in emails:
            validEmails.add(emailValidator(email))
        return len(validEmails)