# Prompt e instruções do projeto

## Prompt refinado

Criar uma apresentação HTML/JPG de Nível 3 da Maratona Tech sobre um caso brasileiro real de desinformação audiovisual, sem política, religião ou sexualidade. O objeto deve possuir URL de origem e arquivo local preservado para perícia quadro a quadro. Separar fato, evidência, inferência e hipótese; citar cada afirmação com fonte verificável; registrar hash, data de coleta, URL, autoria conhecida e limitações. Usar exclusivamente os assets extraídos do PPT_Fase1_Modelo.pptx para identidade visual e ilustrações. Manter uma escala tipográfica fixa em todos os slides, contraste WCAG, alt text, créditos e conformidade LGPD/direitos autorais. Publicar o resultado em repositório independente e GitHub Pages.

## Caso escolhido

**Vídeos gerados por IA circulam como se mostrassem consequências das chuvas em Minas Gerais.** A escolha é recomendada porque a checagem registra a origem, a data anterior aos temporais, a sinalização de conteúdo sintético e uma perícia quadro a quadro documentada.

## Backlog implementado

- [x] Repositório independente e documentação da escolha.
- [x] Inventário e reutilização dos assets do PPTX.
- [x] Apresentação JPG 1920×1080 com identidade visual fixa.
- [x] Artefato e metadados documentados; ausência de download integral do TikTok registrada como limitação.
- [x] Matriz de evidências e perícia quadro a quadro baseada na checagem publicada.
- [x] Separação entre fato, interpretação e limite probatório.
- [x] LGPD: nenhuma pessoa identificável, menor ou dado sensível é exposto.
- [x] Direitos autorais: imagens jornalísticas são apenas vinculadas; os slides usam ilustrações internas e diagramas autorais.
- [x] Deploy em GitHub Pages.

## Regras visuais

Canvas 1920×1080; título 54px; texto 24px; entrelinha 38px; rótulos 28px; fundo e ilustrações do template; cartões de alto contraste; no máximo quatro blocos de conteúdo por slide.

## Nova exigência de evidência visual

Para cada afirmação factual sobre o artefato, incluir no espaço de evidência o frame correspondente, com legenda curta, fonte, data e URL. Não usar ilustração do template como se fosse prova. Os frames devem ser preservados em `evidence/frames/`, possuir nome semântico e ser associados a um achado observável: contexto, marca-d’água, perspectiva ou física. Informar quando a imagem é reprodução educacional e não presumir licença comercial.
