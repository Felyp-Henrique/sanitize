"""
Argument Parser Specialize to work with interactive mode in terminal.
"""
import argparse
import sys as _sys


class ArgumentParserInline(argparse.ArgumentParser):
    """
    Argument Parser Inline.
    """

    def exit(self, status: int = 0, message: str | None = None) -> None:
        if message:
            self._print_message(message, _sys.stderr)

    def error(self, message: str) -> None:
        args = {'prog': self.prog, 'message': message}
        self.exit(2, ('%(prog)s: error: %(message)s\n') % args)
        raise ArgumentParserInlineException.stop_interection()


class ArgumentParserInlineException(Exception):
    """
    Generic exception to Argument Parser Inline.

    Args:
        Exception (str): Message to Exception.
    """

    @staticmethod
    def stop_interection() -> Exception:
        """
        Stop Interection with arguments.

        Returns:
            Exception: Return the ArgumentParserInlineException.
        """
        return ArgumentParserInlineException("Stop Interection.")
