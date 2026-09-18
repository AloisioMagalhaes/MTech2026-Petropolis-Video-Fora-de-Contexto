# Foco em tela cheia

O HTML oferece foco individual no JPG do slide selecionado. O botão **Tela cheia** aplica a Fullscreen API ao slide ativo; duplo clique ou `Enter`/`Espaço` sobre qualquer imagem produz o mesmo resultado. `Esc` encerra o modo de tela cheia.

O slide mantém proporção 16:9 com `object-fit: contain`, fundo azul-marinho e preenchimento, evitando cortes ou distorções. O botão possui foco visível e nome acessível. Navegadores que não implementam a Fullscreen API permanecem no modo normal sem interromper a apresentação.
