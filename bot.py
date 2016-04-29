from selenium import webdriver

driver = webdriver.Firefox()
page = "http://paginas.seccionamarilla.com.mx/alta-calidad-en-plomeria-y-drenaje-la-hormiga/plomeros-profesionales/distrito-federal/ciudad-de-mexico/benito-juarez/-/"
print "Cargando " + page
driver.get(page)
selector = "#sb-module-7802085 > div > div > div > p:nth-child(5) > a"
print "Buscando selector"
objeto = driver.find_element_by_css_selector(selector)
print objeto.text