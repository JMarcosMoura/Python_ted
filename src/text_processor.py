import re
from pathlib import Path

class TextProcessor:
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.text = self._read_file()
    
    def _read_file(self):
        """Lê o arquivo de texto com tratamento de erros robusto"""
        try:
            return self.file_path.read_text(encoding='utf-8')
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo não encontrado: {self.file_path}")
        except UnicodeDecodeError:
            raise UnicodeDecodeError(f"Problema de codificação no arquivo: {self.file_path}")
    
    def filter_by_start(self, letter: str) -> list:
        """Retorna palavras que começam com a letra especificada"""
        pattern = rf'\b{re.escape(letter)}\w*\b'
        return re.findall(pattern, self.text, re.IGNORECASE)
    
    def filter_by_contain(self, letter: str) -> list:
        """Retorna palavras únicas que contêm a letra especificada"""
        seen = set()
        result = []
        for word in re.findall(r'\b\w+\b', self.text):
            if letter.lower() in word.lower() and word.lower() not in seen:
                seen.add(word.lower())  # considera igual se for a mesma palavra ignorando maiúsculas/minúsculas
                result.append(word)
        return result
    
    def replace_commas(self) -> str:
        """Substitui todas as vírgulas por pontos"""
        return self.text.replace(',', '.')
    
    def extract_dates(self) -> list:
        """Extrai datas nos formatos comuns (dd/mm/aaaa, dd-mm-aaaa, etc.)"""
        pattern = r'\b(\d{1,2}[-/]\d{1,2}[-/]\d{2,4})\b'
        return re.findall(pattern, self.text)
    
    # Dunder methods
    def __str__(self) -> str:
        return f"Processador de Texto: {self.file_path.name}"
    
    def __repr__(self) -> str:
        return f"TextProcessor(file_path='{self.file_path}')"
    
    def __len__(self) -> int:
        """Retorna o número de caracteres no texto"""
        return len(self.text)