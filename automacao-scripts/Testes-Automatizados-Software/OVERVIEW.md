# 📚 Visão Geral de Testes de Software

---

## 📖 Introdução aos Testes de Software

### Definição
Testes de software são processos sistemáticos que visam verificar se o software desenvolvido atende aos requisitos especificados e identificar defeitos para que possam ser corrigidos antes da entrega final. O principal objetivo é garantir que o sistema funcione corretamente, seja confiável, seguro e atenda às expectativas dos usuários.

### Ciclo de Vida de Testes (STLC)
O ciclo de vida de testes acompanha o ciclo de vida de desenvolvimento do software (SDLC) e inclui as seguintes fases:
1. **Planejamento de Testes:** Definição de estratégias, escopo, recursos e cronograma.
2. **Design de Testes:** Criação de casos de teste e preparação do ambiente.
3. **Execução de Testes:** Realização dos testes e registro dos resultados.
4. **Relatório de Testes:** Análise dos resultados, identificação de defeitos e elaboração de relatórios para stakeholders.

> A integração dos testes no ciclo de desenvolvimento permite detectar e corrigir problemas mais cedo, reduzindo custos e evitando retrabalho.

---

## 🗂️ Tipos de Testes de Software

| Tipo de Teste | Descrição |
| :--- | :--- |
| **Testes Unitários** | Verificam a menor parte do software, como funções ou métodos, isoladamente. |
| **Testes de Integração** | Avaliam como diferentes módulos ou serviços funcionam juntos. |
| **Testes de Sistema** | Testam o sistema completo para verificar se ele atende aos requisitos especificados. |
| **Testes de Aceitação** | Conduzidos com a participação do cliente para garantir que o sistema atenda às suas expectativas. |
| **Testes de Regressão** | Realizados após modificações no software para garantir a estabilidade das funções já existentes. |
| **Testes de Desempenho** | Testam velocidade, escalabilidade, estabilidade e o uso de recursos. |
| **Testes de Carga** | Avaliam como o sistema se comporta sob uma carga de trabalho significativa. |
| **Testes de Stress** | Determinam os limites do software, avaliando seu comportamento sob condições extremas. |
| **Testes de Segurança** | Garantem que o software está protegido contra possíveis ameaças e vulnerabilidades. |
| **Testes de Usabilidade** | Focam na experiência e facilidade de uso para o usuário. |
| **Testes End-To-End (E2E)** | Simulam o fluxo completo de uma aplicação. |

---

### 🟢 Testes Funcionais
Concentram-se em verificar se as funcionalidades do software operam conforme o esperado e de acordo com os requisitos:
* **Testes de Unidade:** Essenciais para garantir que cada parte do software funcione corretamente antes da integração.
* **Testes de Integração:** Detectam problemas de interface e dependência entre módulos.
* **Testes de Sistema:** O software é validado em um ambiente que simula condições reais.
* **Testes de Aceitação:** O sucesso nesses testes é um pré-requisito para a entrega final do software.
* **Testes End-To-End:** Verificam a integração de todos os componentes e o fluxo completo do ponto de vista do usuário.

### 🟡 Testes Não Funcionais
Avaliam atributos de qualidade que não estão diretamente ligados às regras de negócio:
* **Desempenho:** Medem a capacidade do software de funcionar sob diferentes cargas.
* **Segurança:** Avaliam a resistência a ataques, incluindo verificação de vulnerabilidades e testes de penetração.
* **Usabilidade:** Garantem que o software seja intuitivo e eficiente.
* **Stress:** Vão além das condições normais de operação, forçando o sistema até a falha para observar o comportamento em colapso.
* **Carga:** Entendem a capacidade de lidar com grande número de usuários simultâneos, identificando gargalos.

---

## 🔄 Testes de Regressão

Realizados após modificações no código (como correções de bugs ou novas funcionalidades). O objetivo é garantir que as alterações não tenham introduzido novos defeitos em partes que estavam funcionando.

**Por que são importantes?**
1.  **Manutenção da Estabilidade:** Garantem que mudanças não comprometam o sistema ao longo do tempo.
2.  **Detecção de Defeitos Introduzidos:** Evitam que pequenas alterações gerem efeitos colaterais inesperados.
3.  **Economia de Tempo e Recursos:** A automação permite que grandes volumes de testes sejam executados rapidamente.

**Como são implementados?**
* **Automatização:** Uso de ferramentas como Selenium, JUnit e pytest.
* **Seleção de Casos:** Foco em áreas impactadas e funcionalidades críticas.
* **Regressão Total vs. Parcial:** Execução de toda a suíte de testes ou apenas da seleção relevante, dependendo do impacto da mudança.

---

## 🛠️ Ferramentas e Práticas

### Ferramentas de Automação
* **Selenium:** Automação de testes em aplicações web, simulando a interação do usuário com o navegador.
* **JUnit e pytest:** Ferramentas para testes unitários automatizados em Java e Python, respectivamente.

### Práticas de Qualidade
* **Test-Driven Development (TDD):** Escrever testes antes de implementar o código, incentivando códigos simples e testáveis.
* **CI/CD:** Integração e entrega contínuas. Testes são executados automaticamente a cada alteração, mantendo o software sempre pronto para produção.
* **DevOps:** Testes integrados em todas as fases do ciclo de vida do software, promovendo a cultura de qualidade contínua.

---

## 🚀 O Framework Pytest

O `pytest` é um framework para Python que facilita a criação e execução de testes automatizados, amplamente utilizado por sua eficiência e robustez.

### Principais Características
* **Simplicidade:** Permite escrever testes de maneira intuitiva usando apenas funções comuns, sem a obrigação de classes complexas.
* **Detecção Automática:** Encontra automaticamente arquivos e funções seguindo convenções de nomeação (ex: `test_*.py`).
* **Assertivas Melhoradas:** Ao usar o `assert` nativo, o pytest gera mensagens de erro detalhadas, facilitando a depuração.
* **Fixtures:** Funções especiais para configurar estados ou dados antes dos testes, permitindo a reutilização de código em ambientes complexos.
* **Plugins:** Vasta coleção de extensões (ex: `pytest-cov` para cobertura, `pytest-xdist` para execução paralela).
* **Integração com CI/CD:** Funciona perfeitamente com GitHub Actions, Jenkins, Travis CI, entre outros pipelines automáticos.

### Exemplo Prático de Teste Unitário
```python
# Exemplo de rquivo: test_example.py

def func(x):
    return x + 1

def test_func():
    assert func(3) == 4