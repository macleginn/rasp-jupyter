from io import StringIO
from contextlib import redirect_stdout

from ipykernel.kernelbase import Kernel
from .RASP.RASP_support.REPL import REPL
# from .RASP.RASP_support.REPL import Stop


class RASPREPLForJupyter(REPL):
    def __init__(self):
        super().__init__()

    def execute(self, code):
        # RASP REPL expects the input to have the readline method,
        # so we wrap the code in a StringIO object
        # to simulate that.
        output_buffer = StringIO()
        with StringIO(code) as input_buffer, redirect_stdout(output_buffer):
            self.run(fromfile=input_buffer, env=self.base_env)
        return output_buffer.getvalue()


rasp_repl = RASPREPLForJupyter()


class RASPKernel(Kernel):
    implementation = 'RASP'
    implementation_version = '1.0'
    language = 'no-op'
    language_version = '0.1'
    language_info = {
        'name': 'Any text',
        'mimetype': 'text/plain',
        'file_extension': '.txt',
    }
    banner = "RASP Kernel"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            # Execute the code using the RASP REPL
            result = rasp_repl.execute(code)
            stream_content = {'name': 'stdout', 'text': result}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {
            'status': 'ok',
            # The base class increments the execution count
            'execution_count': self.execution_count,
            'payload': [],
            'user_expressions': {}
        }


def main():
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=RASPKernel)

if __name__ == '__main__':
    main()
