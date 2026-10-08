# Visita virtual a instalações industriais

Comparar representações de uma instalação para visitas virtuais.

## Implementação atual

Planos de treinamento Nerfacto e Splatfacto; avaliação de imagens por MSE e PSNR.

O código prepara comandos de treinamento por cena. A demonstração calcula métricas em imagens sintéticas; não treina NeRF ou Gaussian Splatting. Treinamento real depende de fotos, poses e ambiente compatível.

## Reproduzir a demonstração sintética

```bash
python demo.py
python -m unittest discover -s tests -v
```

A demonstração usa apenas a biblioteca padrão. O JSON identifica dados sintéticos e limitações. Não há métricas validadas em fotografias reais.

## Dados e treinamento

O código prepara comandos de treinamento por cena. A demonstração calcula métricas em imagens sintéticas; não treina NeRF ou Gaussian Splatting. Treinamento real depende de fotos, poses e ambiente compatível.

## Fluxo real opcional

Instale Nerfstudio no ambiente compatível descrito na documentação. Prepare fotografias e poses no formato Nerfstudio (`transforms.json`). Gere planos:

```bash
python pipeline.py --data /caminho/cena --method nerfacto
python pipeline.py --data /caminho/cena --method splatfacto
```

Acrescente `--execute` para treinar. Compare usando vistas de teste separadas. A demo não produz imagens destes modelos nem estabelece um vencedor.

## Próximas etapas

Executar o fluxo em imagens autorizadas, separar avaliação, documentar falhas e publicar métricas reais.

## Referência técnica

[Documentação oficial](https://docs.nerf.studio/nerfology/methods/splat.html).
