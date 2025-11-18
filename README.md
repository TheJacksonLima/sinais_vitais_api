# 🧬 Sinais Vitais API  
### Simulação de sinais vitais para integração com aplicativos (Wear OS, Mobile, Web)

---

## 📖 Visão Geral  
Esta API foi desenvolvida em **Python + FastAPI** para simular sinais vitais, permitindo testar aplicativos que dependem de leituras contínuas como **BPM (batimentos cardíacos)**, **SpO₂ (oxigenação)** e o **estado do usuário** — que pode variar entre:

- `normal`
- `alerta`
- `zumbi` 🧟‍♂️

Ela foi criada como backend para o aplicativo *Sentinel Life*, mas pode ser usada em qualquer projeto.

---

## ⚙️ Funcionalidades

- ✔️ Simulação automática de sinais vitais  
- ✔️ Ciclo contínuo de estados (normal → alerta → zumbi)  
- ✔️ Endpoint para registrar eventos de “estado zumbi”  
- ✔️ 100% compatível com qualquer cliente HTTP (Ktor, Axios, Retrofit, fetch…)  
- ✔️ Código simples, limpo e totalmente modificável  

---

## 🧪 Endpoints

### 🔹 `GET /`
Verifica se a API está ativa.

### 🔹 `GET /monitor`
Retorna um JSON contendo:

```json
{
  "bpm": 75,
  "spo2": 97,
  "estado": "normal"
}
