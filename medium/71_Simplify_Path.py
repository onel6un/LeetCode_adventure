class Solution:
    stack = []

    def simplifyPath(self, path: str) -> str:
        """Функция приводит абсолютный путь к относительному"""
        self._pars_path(path)
        return self._get_canonical_path()

    def _get_canonical_path(self) -> str:
        return "/" + "/".join(self.stack)

    def _pars_path(self, path: str):
        word = ""
        for s in path:
            if s == "/":
                if not word:
                    continue
                if word == "..":
                    self._pop()
                    word = ""
                elif word == ".":
                    word = ""
                else:
                    self.stack.append(word)
                    word = ""
            else:
                word = word + s

        if word:
            if word == '..':
                self._pop()
            elif word == ".":
                pass
            else:
                self.stack.append(word)

    def _pop(self) -> None:
        if self.stack:
            self.stack.pop()


s = Solution()
print(s.simplifyPath("/..."))
