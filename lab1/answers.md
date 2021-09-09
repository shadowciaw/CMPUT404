1. https://github.com/shadowciaw
2. 2.26.0
3. 2.26.0
4. There is no difference
5. The status code is 301 Moved Permanently. In order to get a 200 status code, you need to visit https://www.google.com/
6. 301 Moved, its returned by -i. When curling with www*, code 418 I'm a teapot is returned.
7. The changes in the output are as follows:
    - Form Contents header contains new lines instead of "<P>No form fields.":
        <DT>X: <i>&lt;type 'instance'&gt;</i>
        <DD>MiniFieldStorage('X', 'Y')
    - Shell environment header contains CONTENT_LENGTH and CONTENT_TYPE descriptions, change in remote port and request method (from GET to POST), and UNIQUE_ID is different
8. The raw url: https://gist.githubusercontent.com/shadowciaw/7c2956ab82b26effd5a046b36672558f/raw/4f863687c6443e52c95ab5997fbb91c0d0545154/cmput404lab1.py