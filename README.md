# SMVE - Social Media Video Editor

## 📺 Projeto
Um editor de vídeo automatizado em Python que transforma vídeos brutos (verticais ou horizontais) em conteúdo pronto para redes sociais com:
- ✂️ Remoção automática de silêncios
- ✨ Transições dinâmicas
- 🎬 Efeitos de atenção
- 📐 Múltiplos layouts (comparação, B-roll, tela dividida, react)
- 🎯 Otimização para cada plataforma (TikTok, Instagram, YouTube)

## 🎯 Features Principais

### ✅ Core
- [x] Upload de vídeos (vertical/horizontal)
- [x] Detecção e remoção de silêncios
- [x] Aplicação de transições automáticas
- [ ] Adição de efeitos de atenção
- [ ] Exportação em múltiplos formatos

### 🎬 Presets de Edição
- [ ] **Comparação** - Lado a lado (antes/depois)
- [ ] **B-Roll** - Inserir vídeos secundários
- [ ] **Split Screen** - Tela dividida em até 4 seções
- [ ] **React** - Reação com webcam + vídeo principal
- [ ] **Zoom & Pan** - Ken Burns effect
- [ ] **Picture in Picture** - Overlay com redimensionamento

### 🛠️ Utilitários
- [ ] Gerenciamento de uploads
- [ ] Exportação em resoluções (720p, 1080p, 4K)
- [ ] Batch processing
- [ ] Histórico de edições

## 🏗️ Stack Tecnológico
- **Backend:** FastAPI / Flask
- **Vídeo:** MoviePy, FFmpeg
- **Áudio:** librosa, pydub
- **Visão Computacional:** OpenCV
- **Interface:** Streamlit (MVP) / React (futuro)
- **Banco de Dados:** SQLite / PostgreSQL

## 📦 Instalação

```bash
# Clone o repositório
git clone https://github.com/r4rafael/SMVE-social-media-video-editor.git
cd SMVE-social-media-video-editor

# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Instale FFmpeg (necessário)
# Ubuntu/Debian: sudo apt-get install ffmpeg
# macOS: brew install ffmpeg
# Windows: Download em https://ffmpeg.org/download.html
```

## 🚀 Como Usar

```bash
# Inicie a aplicação
python app.py

# Acesse http://localhost:8000
```

## 📊 Roadmap

### Phase 1: MVP (Semanas 1-3)
- [x] Setup inicial e estrutura
- [ ] Implementar silence remover
- [ ] Adicionar transições básicas (fade in/out)
- [ ] Upload simples de vídeos
- [ ] Exportação básica
- **Entrega:** CLI funcional + Streamlit MVP

### Phase 2: Core Features (Semanas 4-6)
- [ ] Preset: Comparação
- [ ] Preset: Split Screen (2 vídeos)
- [ ] Efeitos de zoom automático
- [ ] Detecção de cenas (para B-roll)
- [ ] Interface Streamlit completa
- **Entrega:** 3 presets funcionando

### Phase 3: Advanced Features (Semanas 7-9)
- [ ] Preset: React
- [ ] Preset: B-roll automático
- [ ] Efeitos de atenção (pulse, glitch, etc)
- [ ] Transições avançadas (30+ tipos)
- [ ] Otimização de performance
- **Entrega:** Todos os presets + efeitos

### Phase 4: Backend & API (Semanas 10-12)
- [ ] FastAPI / Flask backend
- [ ] Autenticação de usuários
- [ ] Banco de dados (projetos, histórico)
- [ ] Fila de processamento (Celery)
- [ ] Webhook para status de edição
- **Entrega:** API REST completa

### Phase 5: Frontend Web (Semanas 13-16)
- [ ] React interface (drag & drop)
- [ ] Preview em tempo real
- [ ] Galleria de templates
- [ ] Integração com redes sociais
- [ ] Hospedagem na nuvem (AWS/GCP)
- **Entrega:** Aplicação web funcional

### Phase 6: Monetização & Polish (Semanas 17+)
- [ ] Planos de subscription
- [ ] Analytics e métricas
- [ ] Suporte a plugins custom
- [ ] Mobile app
- [ ] Marketplace de templates

## 📁 Estrutura do Projeto

```
SMVE-social-media-video-editor/
├── app.py                    # Entry point principal
├── requirements.txt          # Dependências
├── .gitignore               # Configuração Git
├── README.md                # Este arquivo
├── core/
│   ├── __init__.py
│   ├── silence_remover.py   # Remoção de silêncios
│   ├── editor.py            # Lógica principal de edição
│   └── effects.py           # Biblioteca de efeitos
├── presets/
│   ├── __init__.py
│   ├── comparison.py        # Comparação lado a lado
│   ├── broll.py             # B-roll automático
│   ├── split_screen.py      # Tela dividida
│   ├── react.py             # React/Reação
│   └── transitions.py       # Transições
├── utils/
│   ├── __init__.py
│   ├── upload.py            # Gerenciamento de uploads
│   ├── export.py            # Exportação de vídeos
│   └── helpers.py           # Funções auxiliares
├── config/
│   ├── __init__.py
│   └── settings.py          # Configurações
├── tests/                   # Testes unitários
├── docs/                    # Documentação
└── assets/                  # Assets (templates, ícones)
```

## 🔧 Configuração

Crie um arquivo `.env` na raiz do projeto:

```env
DEBUG=True
VIDEO_UPLOAD_FOLDER=uploads/
VIDEO_OUTPUT_FOLDER=outputs/
MAX_FILE_SIZE=500MB
SUPPORTED_FORMATS=mp4,mov,avi,mkv
```

## 🧪 Testes

```bash
pytest tests/
```

## 📝 Licença
MIT License

## 🤝 Contribuições
Contribuições são bem-vindas! Abra uma issue ou PR.

## 📧 Contato
Para dúvidas ou sugestões, abra uma issue no repositório.

---

**Status:** 🟡 Em Desenvolvimento
**Última Atualização:** 21/04/2026