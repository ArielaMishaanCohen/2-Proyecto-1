
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time, os

# Configurar carpeta de descargas
descargas_dir = os.path.abspath("mineduc_excels")
os.makedirs(descargas_dir, exist_ok=True)

# Configurar Chrome con modo no detectado
options = uc.ChromeOptions()
options.add_experimental_option("prefs", {
    "download.default_directory": descargas_dir,
    "download.prompt_for_download": False,
    "safebrowsing.enabled": True
})
options.add_argument("--start-maximized")

# Crear navegador disfrazado
driver = uc.Chrome(options=options)
wait = WebDriverWait(driver, 20)

# Ir al sitio
driver.get("https://www.mineduc.gob.gt/BUSCAESTABLECIMIENTO_GE/")

# Esperar el menú de departamentos
try:
    select_elem = wait.until(EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_ddlDepartamento")))
    select_depto = Select(select_elem)

    print("✅ Menú de departamentos cargado")

except Exception as e:
    print("❌ No se pudo cargar el menú de departamentos")
    print(e)
    driver.quit()
    exit()
    

'''from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os

# Configurar la carpeta de descargas
descargas_dir = os.path.abspath("mineduc_excels")
os.makedirs(descargas_dir, exist_ok=True)

# Configurar opciones del navegador
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": descargas_dir,
    "download.prompt_for_download": False,
    "safebrowsing.enabled": True
})
chrome_options.add_argument("--start-maximized")

# Iniciar navegador
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 20)

# Ir a la página principal
driver.get("https://www.mineduc.gob.gt/BUSCAESTABLECIMIENTO_GE/")

# Esperar a que cargue el combo de departamentos
select_element = wait.until(EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_ddlDepartamento")))
select_depto = Select(select_element)

# Recorrer cada departamento (saltando la opción vacía)
for i, option in enumerate(select_depto.options):
    depto_valor = option.get_attribute("value")
    if not depto_valor:
        continue

    print(f"\n🔍 Procesando departamento {option.text} ({depto_valor})")

    # Seleccionar departamento
    select_depto.select_by_value(depto_valor)

    # Clic en "Buscar"
    btn_buscar = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnBuscar")
    btn_buscar.click()

    # Esperar la tabla de resultados
    try:
        tabla = wait.until(EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_gvResultado")))
        filas = tabla.find_elements(By.TAG_NAME, "tr")[1:]  # saltar encabezado

        print(f"➡️  {len(filas)} centros encontrados")

        for j, fila in enumerate(filas):
            try:
                print(f"  [{j+1}/{len(filas)}] Descargando Excel...")

                # Buscar botón "Seleccionar centro"
                boton = fila.find_element(By.LINK_TEXT, "Seleccionar centro")
                boton.click()

                # Esperar el botón de descarga
                btn_descargar = wait.until(EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_btnDescargar")))
                btn_descargar.click()

                # Esperar un poco para asegurar descarga
                time.sleep(3)

                # Cerrar detalle (volver)
                btn_regresar = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnRegresar")
                btn_regresar.click()

                # Volver a obtener referencias a la tabla y filas, porque se recarga
                tabla = wait.until(EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_gvResultado")))
                filas = tabla.find_elements(By.TAG_NAME, "tr")[1:]

            except Exception as e:
                print(f"    ⚠️ Error en centro #{j+1}: {e}")
                # Volver al buscador en caso de error
                driver.get("https://www.mineduc.gob.gt/BUSCAESTABLECIMIENTO_GE/")
                select_depto = Select(wait.until(EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_ddlDepartamento"))))
                select_depto.select_by_value(depto_valor)
                btn_buscar = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnBuscar")
                btn_buscar.click()
                tabla = wait.until(EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_gvResultado")))
                filas = tabla.find_elements(By.TAG_NAME, "tr")[1:]
                continue

    except Exception as e:
        print(f"❌ No se encontraron centros para {option.text}: {e}")
        continue

# Finalizar
driver.quit()
print("\n✅ Descargas completas.")'''