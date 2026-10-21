import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

load_dotenv()
driver_path = os.environ.get('PATH_DRIVE_BROWSER')
service = Service(driver_path)

driver = webdriver.Firefox(service=service)
try:
    driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_alert")

    # WebDriverWait(driver, 10): espera EXPLÍCITA de até 10s.
    # Diferente de time.sleep() (fixo), ela para assim que a condição for atendida.
    wait = WebDriverWait(driver, 10)

    # current_window_handle retorna uma STRING (identificador único da aba), não um objeto.
    # Por isso, use driver.title / driver.current_url para obter info da aba ativa.
    original = driver.current_window_handle

    # EC.frame_to_be_available_and_switch_to_it: espera o iframe carregar E já entra nele.
    # Após isso, find_element busca DENTRO do iframe, não na página principal.
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "iframeResult")))

    titulo = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h2")))
    assert titulo.text == "JavaScript Alert"
    print(40 * "-")
    print(f"Titulo h2 ({titulo.text})")

    driver.find_element(By.TAG_NAME, "button").click()

    # EC.alert_is_present(): espera até um alerta JS aparecer e retorna o objeto do alerta.
    # O objeto tem .text (ler texto), .accept() (OK), .dismiss() (Cancelar), .send_keys() (prompt).
    alerta = wait.until(EC.alert_is_present())
    assert "alert" in alerta.text.lower(), \
        f"Texto inesperado no alerta: {alerta.text}"
    print(f"✅ Alerta capturado: {alerta.text}")
    alerta.accept()

    # Sai do iframe e volta para o documento principal (top-level).
    # Sem isso, find_element buscaria dentro do iframe (onde não há mais botão).
    driver.switch_to.default_content()
    print(f"Aba original: {driver.title} | URL: {driver.current_url}")

    # Abre uma NOVA aba e já troca o foco para ela (Selenium 4+).
    # "tab" = aba; "window" = janela separada.
    driver.switch_to.new_window("tab")
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    titulo_aba2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content h3")))
    print(40 * "-")
    print(f"Aba nova: {driver.title} | URL: {driver.current_url}")
    print(f"Titulo aba nova: ({titulo_aba2.text})")
    print(40 * "-")
    botao = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button")))
    botao.click()

    # EC.invisibility_of_element_located: espera até o elemento ficar INVISÍVEL
    # (display:none) ou ser removido do DOM. Retorna True quando desaparece.
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "#start button")))
    print("✅ Botão sumiu da página (invisível)")

    # Verificar com is_displayed() (se ainda encontrar no DOM)
    try:
        botao = driver.find_element(By.CSS_SELECTOR, "#start button")
        # is_displayed() retorna False se o elemento estiver oculto (display:none).
        # find_element ainda encontra o elemento (ele está no DOM), mas is_displayed() = False.
        assert not botao.is_displayed(), "Botão ainda visível!"
        print("✅ is_displayed() = False (confirmado, botão invisivel)")
    except NoSuchElementException:
        print("✅ Botão foi removido do DOM completamente")

    texto_escondido = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4")))
    assert "hello" in texto_escondido.text.lower(), \
        f"a mensagem inesperada : {texto_escondido.text}"
    print(f"a mensagem escondida apos o 'start' é : {texto_escondido.text}")

    # Fecha a aba atual (a nova). Depois, troca o foco de volta para a aba original
    # usando o handle salvo em 'original' (linha 19).
    driver.close()
    driver.switch_to.window(original)
    print(40 * "-")

    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "iframeResult")))
    titulo = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h2")))
    assert titulo.text == "JavaScript Alert"
    print(f"Titulo h2 ({titulo.text})")
    driver.switch_to.default_content()
    print(f"Voltou para aba original: {driver.title} | URL: {driver.current_url}")
    print(40 * "-")

except TimeoutException:
    driver.save_screenshot("timeout.png")
    print("❌ Timeout: elemento não apareceu em 10 segundos")
    raise

finally:
    try:
        driver.quit()
    except Exception:
        pass  # Sessão já encerrada pelo close() — ignorar
