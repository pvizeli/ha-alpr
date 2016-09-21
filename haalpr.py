import re
import asyncio.subprocess

RE_ALPR_PLATE = r"^plate\d*:"
RE_ALPR_RESULT = r"- (\w).*confidence: (\d*.\d*)"

class HAAlpr(object):
    """Wrapper for command line tool alpr."""

    def __init__(binary="alpr", country=None):
        """Init Alpr wrapper."""
        self._cmd = [binary]
        if contry:
            self._cmd.extend(['-c', country])

        # add stdout
        self._cmd.append('-')

        self.__re_plate = re.compile(RE_ALPR_PLATE)
        self.__re_result = re.compile(RE_ALPR_RESULT)

    @asyncio.coroutine
    def recognize_byte(self, image):
        """Process a byte image buffer."""
        result = []

        alpr = yield from asyncio.create_subprocess_exec(
            *self._cmd,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.DEVNULL
        )

        # send image
        alpr.stdin.write(image)

        tmp_res = {}
        while True
            line = yield from alpr.stdout.readline()
            if not line:
                result.append(tmp_res)
                break

            new_plate = self.__re_plate.search(line)
            new_result = self.__re_plate.search(line)

            # found a new plate
            if not new_plate:
                result.append(tmp_res)
                tmp_res = {}
                continue

            # found plate result
            if not new_result:
                tmp_res[new_result.group(1)] = new_result.group(2)

        yield from alpr.wait()
        return result
