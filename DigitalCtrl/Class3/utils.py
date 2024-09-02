import matplotlib.pyplot as plt
import numpy as np
from sympy import pprint, simplify
import lcapy as lc 
from lcapy.discretetime import n, z
from lcapy import UnitImpulse, UnitStep
import re 
from numpy import cos, sin

def PlotExpr(n_values, expr, LIM=10):
    """
    Converte uma expressão UnitImpulse do lcapy em um impulso unitário numérico e plota usando stem.

    Parameters:
    expr (Expr): Expressão UnitImpulse(n - k) do lcapy.
    """

    expr_str = str(expr)
    impulse = np.zeros(len(n_values))
    step = np.zeros(len(n_values))
    
    # Verifica se a string contém 'UnitImpulse'
    if 'UnitImpulse' in expr_str:
        # Extrai o deslocamento (shift) do impulso a partir da string
        shift_str = expr_str.split('UnitImpulse(')[1].split(')')[0].strip()
        
        try:
            # Converte o deslocamento para inteiro
            shift_str = shift_str.replace('n', '0')
            shift = int(eval(shift_str))
        except ValueError:
            print("Erro: Deslocamento não é um inteiro válido.")
            return
        

        impulse = np.zeros(len(n_values))
        
        # Coloca o impulso na posição correta com base no deslocamento
        if (shift + LIM) < len(impulse) and (shift + LIM) >= 0:
            impulse[shift + LIM] = 1
        
    if 'UnitStep' in expr_str:
        # Extrai o deslocamento (shift) do passo a partir da string
        shift_str = expr_str.split('UnitStep(')[1].split(')')[0].strip()
        
        try:
            # Converte o deslocamento para inteiro
            shift_str = shift_str.replace('n', '0')
            shift = int(eval(shift_str))
        except ValueError:
            print("Erro: Deslocamento não é um inteiro válido.")
            return np.zeros(len(n_values))
        
        # Cria o vetor da função de passo unitário
        step = np.zeros(len(n_values))
        
        # Preenche a função de passo com base no deslocamento
        step[n_values >= shift] = 1
    
    
    # Verifica se a expressão contém 'UnitImpulse' ou 'UnitStep'
    expr_str = re.sub(r'UnitImpulse\([^)]*\)', 'impulse', expr_str)
    expr_str = re.sub(r'UnitStep\([^)]*\)', 'step', expr_str)

    # replace n by 0 
    expr_str = expr_str.replace('n', 'n_values')


    # Cria um contexto para avaliação com base nas variáveis presentes na expressão
    context = {}
    context_test = {
        'impulse': impulse,
        'step': step,
        'cos': cos,
        'sin': sin,
        'n_values': n_values
    }
    # Adiciona variáveis ao contexto com base no dicionário
    for key, value in context_test.items():
        if key in expr_str:
            context[key] = value

    try:
        # Avalia a expressão
        signal = eval(expr_str, context)
    except Exception as e:
        print(f"Erro ao avaliar a expressão: {e}")
        raise e
        return None

    return signal