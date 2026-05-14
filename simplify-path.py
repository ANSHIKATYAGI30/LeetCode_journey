class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        stack = []

        # Split path by '/'
        parts = path.split('/')

        for part in parts:

            # Ignore empty and '.'
            if part == '' or part == '.':
                continue

            # Go to parent directory
            elif part == '..':

                if stack:
                    stack.pop()

            # Valid directory name
            else:
                stack.append(part)

        # Build final path
        return '/' + '/'.join(stack)
