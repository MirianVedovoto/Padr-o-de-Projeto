# 1. Destinatário (Receiver): A lógica de negócio
class TextEditor:
    def __init__(self):
        self.text = ""

    def add_text(self, new_content):
        self.text += new_content
        print(f"Editor: Adicionado '{new_content}'. Texto atual: '{self.text}'")

    def delete_last(self, length):
        if len(self.text) >= length:
            self.text = self.text[:-length]
        else:
            self.text = ""
        print(f"Editor: Apagado {length} caracteres. Texto atual: '{self.text}'")

# 2. Interface Comando
class Command(ABC):
    @abstractmethod
    def execute(self):
        """Executa a operação."""
        pass
    
    # Em um sistema real, comandos que alteram o estado teriam um método undo()

# 3. Comandos Concretos
class AddTextCommand(Command):
    def __init__(self, editor: TextEditor, content: str):
        self.editor = editor
        self.content = content
    
    def execute(self):
        print(f"Comando: Executando 'Adicionar Texto'")
        self.editor.add_text(self.content)

class DeleteCommand(Command):
    def __init__(self, editor: TextEditor, length: int):
        self.editor = editor
        self.length = length

    def execute(self):
        print(f"Comando: Executando 'Apagar'")
        self.editor.delete_last(self.length)

# 4. Remetente (Invoker): Não conhece o Destinatário, só o Comando
class Button:
    def __init__(self):
        self.command = None

    def set_command(self, command: Command):
        self.command = command

    def click(self):
        if self.command:
            print("Botão Clicado.")
            self.command.execute()
        else:
            print("Botão sem comando associado.")

# CLIENTE (Configuração e Uso)
if __name__ == "__main__":
    editor = TextEditor()
    
    # 1. Criação dos Comandos, associando o Destinatário (editor)
    cmd_write_hello = AddTextCommand(editor, "Olá Mundo ")
    cmd_delete_word = DeleteCommand(editor, 6)

    # 2. Criação do Remetente (Botão)
    write_button = Button()
    delete_button = Button()
    
    # 3. Associação dos Comandos aos Remetentes
    write_button.set_command(cmd_write_hello)
    delete_button.set_command(cmd_delete_word)

    # Execução: O Invoker (botão) chama o comando
    write_button.click()
    # Output: Editor: Adicionado 'Olá Mundo '. Texto atual: 'Olá Mundo '
    
    delete_button.click()
    # Output: Editor: Apagado 6 caracteres. Texto atual: 'Olá '