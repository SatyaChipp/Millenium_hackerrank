#get possible domain names

# Complete the getPotentialDomains function below.
import re
def getPotentialDomains(lines):
    pattern = '(http|https)\\://(www.|ww2.|)([a-zA-Z0-9\\-\\.]+)(\\.[a-zA-Z]+)(/\\S*)?'

    regex = re.compile(pattern)
    s = set()
    for i in range(len(lines)):
        for string in lines:
            iterator = regex.finditer(string)
            if iterator:
                for match in iterator:
                    s.add((match.group(3) + match.group(4)).replace('web.', ''))
    return (';'.join(t for t in sorted(s)))
