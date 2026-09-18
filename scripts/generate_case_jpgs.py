from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import textwrap

R=Path(__file__).parents[1]; A=R/'assets'; O=R/'slides'; O.mkdir(exist_ok=True)
font_path='C:/Windows/Fonts/arial.ttf'; bold_path='C:/Windows/Fonts/arialbd.ttf'
def ft(n,b=False): return ImageFont.truetype(bold_path if b else font_path,n)
S=[
('CAPA','Vídeo sintético em enchentes',['Maratona Tech 2026 · Nível 3','Caso brasileiro: imagens geradas por IA atribuídas às chuvas em Minas Gerais.'],'template-icones-ilustracoes-007.png'),
('PROBLEMA DIGITAL','O contexto enganoso',['Publicações apresentaram vídeos sintéticos como registros reais das chuvas.','A alegação misturou uma tragédia real com imagens produzidas antes dos temporais.','Objeto: origem, contexto e sinais técnicos do conteúdo.'],'template-icones-ilustracoes-029.png'),
('ARTEFATO DIGITAL','Arquivo e origem',['Registro publicado no TikTok por @caosclimatico em 21 fev. 2026.','A checagem localizou a publicação original e informa a sinalização “gerado por IA”.','URL: https://www.tiktok.com/@caosclimatico · cópia bruta não preservada localmente.'],'template-icones-ilustracoes-008.png'),
('PERÍCIA QUADRO A QUADRO','Indícios observáveis',['Marca-d’água borrada em diferentes momentos.','Contorno da água e estruturas apresentam deformações.','A água se desloca de modo incompatível com a gravidade.'],'template-icones-ilustracoes-026.png'),
('LINHA DO TEMPO','Antes, durante e depois',['21 fev.: publicação original do perfil sintético.','23–24 fev.: temporais atingem municípios mineiros.','26–27 fev.: checagem identifica origem e inconsistências.'],'template-icones-ilustracoes-018.png'),
('EVIDÊNCIA','O que a fonte confirma',['Confirma: origem, data, aviso de conteúdo sintético e indícios visuais.','Não confirma: autoria civil do vídeo, arquivo bruto ou cadeia de custódia.','A conclusão é “conteúdo gerado por IA e fora de contexto”.'],'template-icones-ilustracoes-040.png'),
('CAUSA-RAIZ','Como o engano se amplia',['Conteúdo sintético + legenda de emergência.','Comoção e urgência favorecem compartilhamento.','Plataformas ampliam alcance por interação e recomendação.'],'template-icones-ilustracoes-049.png'),
('IMPACTO','Riscos sociais',['Informacional: percepção falsa do desastre.','Humanitário: atenção desviada durante uma emergência.','Coletivo: redução da confiança em imagens como evidência.'],'template-icones-ilustracoes-075.png'),
('TRIANGULAÇÃO','Fontes independentes',['Aos Fatos: origem e perícia visual.','G1: ocorrência dos temporais e impactos.','CNN Brasil: dimensão das chuvas e vítimas.'],'template-icones-ilustracoes-040.png'),
('MÉTODO','Protocolo reproduzível',['1. Preservar URL e data. 2. Obter o arquivo disponível.','3. Extrair frames em intervalos regulares. 4. Comparar continuidade, física e metadados.','5. Registrar achado, fonte e grau de certeza.'],'template-icones-ilustracoes-100.png'),
('EXPLICAÇÃO TÉCNICA','O que é conteúdo sintético',['Modelos de IA podem gerar ou alterar imagens para simular acontecimentos.','Sinais isolados são indícios; a conclusão exige conjunto de evidências.'],'template-icones-ilustracoes-007.png'),
('LGPD E ÉTICA','Tratamento responsável',['Não expor nomes de vítimas, rostos identificáveis ou dados pessoais.','Usar somente o mínimo necessário para demonstrar a verificação.','Direcionar para a fonte original, sem redistribuir material sensível.'],'template-icones-ilustracoes-106.png'),
('RECOMENDAÇÃO','Antes de compartilhar',['PAUSE: observe a legenda e a data.','CONFIRME: compare fontes independentes.','DENUNCIE: preserve o link e sinalize o conteúdo enganoso.'],'template-icones-ilustracoes-007.png'),
('CONCLUSÃO','Resposta investigativa',['O vídeo não é evidência autêntica das chuvas mineiras.','A perícia publicada combina rastreamento de origem e análise quadro a quadro.','Contexto, fonte e método são necessários para interpretar imagens digitais.'],'template-icones-ilustracoes-007.png'),
('REFERÊNCIAS','Fontes citadas',['AOS FATOS (2026). Vídeos gerados por IA circulam como se mostrassem consequências das chuvas em MG.','G1 (2026). Cobertura dos temporais em Minas Gerais.','CNN BRASIL (2026). Cobertura dos temporais e impactos.','MIRSKY; LEE (2021). The creation and detection of deepfakes. ACM Computing Surveys.'],'template-icones-ilustracoes-107.png')]

def draw_diagram(d,i):
    labels={2:['PUBLICAÇÃO','LEGENDA','INTERPRETAÇÃO'],3:['ORIGINAL','IA','COMPARTILHAMENTO'],4:['FRAME 01','FRAME 02','FRAME 03'],5:['21 FEV','23–24 FEV','26–27 FEV'],6:['CONFIRMADO','LIMITAÇÃO','CONCLUSÃO'],7:['EMOÇÃO','ALCANCE','IMPACTO'],8:['INFORMAÇÃO','SOCIAL','CONFIANÇA'],9:['AOS FATOS','G1','CNN'],10:['PRESERVAR','COMPARAR','REGISTRAR'],11:['GERAR','ALTERAR','VERIFICAR'],12:['MINIMIZAR','ANONIMIZAR','ATRIBUIR'],13:['PAUSAR','CONFIRMAR','DENUNCIAR']}.get(i)
    if not labels:return
    y=820
    for n,label in enumerate(labels):
        x=735+n*365; d.rounded_rectangle((x,y,x+315,y+70),radius=18,fill=(16,42,67),outline=(246,195,68),width=3)
        d.text((x+18,y+20),label,font=ft(23,True),fill='white')
        if n<2:d.line((x+315,y+35,x+365,y+35),fill=(246,195,68),width=5)

for i,(section,title,paras,asset) in enumerate(S,1):
    im=Image.open(A/'template-capa-002.png').convert('RGB').resize((1920,1080)); d=ImageDraw.Draw(im)
    d.rectangle((0,0,1920,18),fill=(47,128,237)); d.rectangle((0,1062,1920,1080),fill=(246,195,68))
    d.rounded_rectangle((680,110,1850,1000),radius=28,fill=(247,251,255)); d.rounded_rectangle((70,220,650,850),radius=32,fill='white',outline=(199,215,229),width=5)
    a=Image.open(A/asset).convert('RGBA'); a.thumbnail((520,560)); im.paste(a,(360-a.width//2,535-a.height//2),a)
    d.text((740,170),section,font=ft(28,True),fill=(47,128,237)); d.text((740,225),title,font=ft(54,True),fill=(16,42,67)); y=330
    for n,p in enumerate(paras,1):
        lines=textwrap.wrap(p,58); h=max(82,38*len(lines)+24); d.rounded_rectangle((735,y,1805,y+h),radius=16,fill=(16,42,67),outline=(246,195,68),width=2); d.ellipse((755,y+18,795,y+58),fill=(246,195,68)); d.text((768,y+22),str(n),font=ft(18,True),fill=(16,42,67))
        for j,line in enumerate(lines): d.text((820,y+17+j*38),line,font=ft(24),fill='white')
        y+=h+18
    draw_diagram(d,i); d.text((110,790),'ILUSTRAÇÃO DO TEMPLATE · APOIO VISUAL',font=ft(13,True),fill=(16,42,67)); d.text((1800,1015),f'{i}/15',font=ft(24),fill=(72,102,129)); im.save(O/f'slide-{i:02d}.jpg',quality=94,optimize=True)
