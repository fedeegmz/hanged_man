from app.application.application import Application
from app.infrastructure.console_impl import ConsoleImpl
from app.infrastructure.word_repository_impl import WordRepositoryImpl

if __name__ == "__main__":
    console = ConsoleImpl()
    word_repository = WordRepositoryImpl()
    application = Application(console, word_repository)

    application.run()
