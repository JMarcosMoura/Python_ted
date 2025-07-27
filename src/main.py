from text_processor import TextProcessor
from pathlib import Path

def main():
    try:
        # Configuração de caminho
        base_dir = Path(__file__).resolve().parent.parent
        file_path = base_dir / 'data' / 'zelda_skyward_sword.txt'
        
        # Validação prévia
        if not file_path.exists():
            raise FileNotFoundError(f"Arquivo de texto não encontrado em: {file_path}")
        
        # Processamento
        processor = TextProcessor(file_path)
        
        # Saída
        print(f"\n{processor}")
        print(f"Tamanho do texto: {len(processor)} caracteres\n")
        
        # Exemplos de operações
        print("Palavras começando com 'p':", processor.filter_by_start('p')[:5])
        print("Palavras contendo 'z':", processor.filter_by_contain('z')[:5])
        print("Datas encontradas:", processor.extract_dates())
        
        processed_text = processor.replace_commas()
        print("\n\nTexto processado (amostra):\n")
        print(processed_text[:500] + "...\n")

    except Exception as e:
        print(f"\nErro durante a execução: {type(e).__name__} - {e}")

if __name__ == "__main__":
    main()