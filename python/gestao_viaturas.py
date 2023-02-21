# # matricula (str), marca, modelo, data
# 10-XY-20,Opel,Corsa XL,2019-10-15
# 20-PQ-15,Mercedes,300SL,2017-05-31

# Menu
#       1 - Listar Viaturas
#       2 - Pesquisar Viaturas
#       3 - Adicionar Viatura
#       4 - Remover Viatura
#       5 - Actualizar Catálogo
#       6 - Recarregar Catálogo
#       T - Terminar
# 
#       Opção >> 

from datetime import date
import datetime
import imp
import subprocess
import sys
import re
from typing import TextIO
import csv


CSV_DEFAULT_DELIM = ','
DEFAULT_INDENTATION = 10


class Viatura:
    def __init__(
            self,
            matricula: str,
            marca: str,
            modelo: str,
            data: date,
    ):    
        if not re.fullmatch(r'(^[0-9]{2}-[A-Z]{2}-[0-9]{2})', matricula):
            raise InvalidProdAttribute(f'{matricula=} inválida (formato errado)')
        if not marca:
            raise InvalidProdAttribute('marca vazia')
        if not modelo:
            raise InvalidProdAttribute('modelo vazia')
        if not datetime.date.fromisoformat(data):
            raise InvalidProdAttribute(f'{data=} inválida (deve ter formato de data ano-mês-dia)')
        
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.data = data
    #:

    @classmethod
    def from_csv(cls, linha: str, delim = CSV_DEFAULT_DELIM) -> 'Viatura':
        attrs = linha.split(delim)
        return cls(
            matricula = attrs[0],
            marca = attrs[1],
            modelo = attrs[2],
            data = attrs[3],
        )
    #:

    def __str__(self) -> str:
            cls_name = self.__class__.__name__
            return f'{cls_name}[matricula= {self.matricula}  marca = "{self.marca}" modelo = "{self.modelo}" '\
                f'data = "{self.data}"]'
    #:

    def __repr__(self) -> str:
        cls_name = self.__class__.__name__
        return f'{cls_name}(matricula={self.matricula}, marca="{self.marca}", modelo="{self.modelo}", '\
                f'data={(self.data)})'
    #:

class InvalidProdAttribute(ValueError):
    pass
#:

class CatalogoViaturas:
    def __init__(self):
        self._viats = {}
    #:

    def append(self, viat: Viatura):
        if viat.matricula in self._viats:
            raise DuplicateValue(f'Já existe viatura com matrícula {viat.matricula} no catálogo')
        self._viats[viat.matricula] = viat
    #:

    def _dump(self):
        for viat in self._viats.values():
            print(viat)
        #:
    #:

    def obtem_por_matricula(self, matricula: str) -> Viatura | None: 
        return self._viats.get(matricula)
    #:

    def pesquisa(self, criterio) -> 'CatalogoViaturas':
        encontradas = CatalogoViaturas()
        for viat in self._viats.values():
            if criterio(viat):
                encontradas.append(viat)
        return encontradas
    #:

    def remove_por_matricula(self, matricula: str) -> Viatura | None:
        viat = self._viats.get(matricula)
        if viat:
            del self._viats[matricula]
        return viat
    #:

    def remove(self, criterio) -> 'CatalogoViaturas':
        a_remover = self.pesquisa(criterio)
        for viat in a_remover:
            del self._viats[viat.matricula]
        return a_remover
    #:

    def __str__(self):
        class_name = self.__class__.__name__
        return f'{class_name}[#viaturas = {len(self._viats)}]'
        #:
    #:

    def __iter__(self):
        for viat in self._viats.values():
            yield viat
    #:

    def __len__(self):
        return len(self._viats)
    #:
#:

class DuplicateValue(Exception):
    pass
#

def le_viaturas(caminho_fich: str, delim = CSV_DEFAULT_DELIM) -> CatalogoViaturas:
    viats = CatalogoViaturas()
    with open(caminho_fich, 'rt') as fich:
        for linha in linhas_relevantes(fich):
            viats.append(Viatura.from_csv(linha, delim))
    return viats
#:

def escreve_viaturas(caminho_fich: str, delim = CSV_DEFAULT_DELIM):
    viats = CatalogoViaturas()
    with open('viaturas.csv', 'w') as fich:
        writer = csv.writer(fich, delim)
        writer.writerows(viats)
        fich.close() 
 #:   

def linhas_relevantes(fich: TextIO):
    for linha in fich:
        linha = linha.strip()
        if len(linha) == 0 or linha[0] == '#':
            continue
        yield linha
#:

def exibe_msg(*args, indent = DEFAULT_INDENTATION, **kargs):
    print(' ' * (indent - 1), *args, **kargs)
#:

def entrada(msg: str, indent = DEFAULT_INDENTATION) -> str:
    return input(f"{' ' * DEFAULT_INDENTATION}{msg}")
#:

def cls():
    if sys.platform == 'win32':
        subprocess.run(['cls'], shell=True, check=True)
    elif sys.platform in ('darwin', 'linux', 'bsd', 'unix'):
        subprocess.run(['clear'], check=True)
    #:
#:

def pause(msg: str="Carregue em ENTER para continuar...", indent = DEFAULT_INDENTATION):
    input(f"{' ' * indent}{msg}")
#:

viaturas = CatalogoViaturas()

def exec_menu():
    """
    - Exibe o catálogo
    - Pesquisa campos
    - Elimina registo
    - Guarda catálogo em ficheiro
    """
    
    while True:
        cls()
        exibe_msg("*******************MENU *******************")
        exibe_msg("* 1 - Listar catálogo                     *")
        exibe_msg("* 2 - Pesquisar por matrícula             *")
        exibe_msg("* 3 - Acrescentar viatura                 *")
        exibe_msg("* 4 - Eliminar viatura                    *")
        exibe_msg("* 5 - Guardar catálogo em ficheiro        *")
        exibe_msg("* 6 - Recarregar catálogo                 *")
        exibe_msg("* T - Terminar programa                   *")
        exibe_msg("*******************************************")

        print()
        
        try:
            opcao = int(entrada("OPÇÃO>> ").strip().upper()) 
            if opcao in (1, 'LISTAR'):
                exec_listar()
            elif opcao in (2, 'PESQUISAR'):
                exec_pesquisar()
            elif opcao in (3, 'ACRESCENTAR'):
                exec_acrescentar()
            elif opcao in (4, 'ELIMINAR'):
                exec_eliminar()
            elif opcao in (5, 'GUARDAR'):
                exec_guardar()  
            elif opcao in (6, 'RECARREGAR'):
                exec_recarregar()
            else:
                 exibe_msg(f"Opção {opcao} inválida!")
        
        except:        
            opcao = entrada("OPÇÃO>> ").strip().upper()
            if opcao in ('T', 'TERMINAR'):
                exec_terminar()
        pause()
        #:
    #:
#:

def exec_listar():
    cabecalho = f'{"Matrícula":^25}|{"Marca":^20}|{"Modelo":^20}|{"Data":^25}'
    separador = f'{"-" * 25}+{"-" * 20}+{"-" * 20}+{"-" * 25}'
    print()
    exibe_msg(cabecalho)
    exibe_msg(separador)
    for viat in viaturas:
        linha = f'{viat.matricula:^25}|{viat.marca:^20}|{viat.modelo:^20}|{viat.data:^25}'
        exibe_msg(linha)
    #:
    exibe_msg(separador)
    print()
    pause()
 #:   

def exec_pesquisar():
    cls()
    matricula = input('Digite a matrícula: ')
    viat = viaturas.obtem_por_matricula(matricula)
    exibe_msg(viat)
    print()
    pause()
#:

def exec_acrescentar():
    while True:
        cls()
        try:
            matricula = input('Digite a matrícula: ')
            marca = input('Digite a marca: ')
            modelo = input('Digite ao modelo: ')
            data = input('Digite a data da matrícula: ')
            
            viat = Viatura(matricula, marca, modelo, data)        
            viaturas.append(viat)
            break

        except InvalidProdAttribute as ex:
            exibe_msg(f"Problemas ao criar viatura:\n{ex}")
            pause()
        except DuplicateValue as ex:
           exibe_msg(f"Viatura {viat.matricula} já existe no catálago.")

    exibe_msg("Viatura adicionada com sucesso")
    print()
    pause()
#:

def exec_eliminar(): 
    while True:
        cls()
        try:   
            matricula = input('Digite a matrícula: ')
            viaturas.remove_por_matricula(matricula)
            break

        except InvalidProdAttribute as ex:
            exibe_msg(f'Matrícula {ex} inexistente.')
            print()
    exibe_msg('Viatura eliminada.')     
    print()
    pause()
#: 

def exec_guardar():
    escreve_viaturas(viaturas)
    exibe_msg('Catálogo guardado.')
    pause()
#:

def exec_recarregar():
    imp.reload = True
    exibe_msg('Catálogo recarregado.')
    print()
    pause()
#:

def exec_terminar():
    sys.exit(0)
#:

def main(): 
    global viaturas
    viaturas = le_viaturas('viaturas.csv')
    exec_menu()
#:

if __name__ == '__main__':
    main()
#:


      

        


    


