import sys, re
src=open(sys.argv[1]).read(); dst=sys.argv[2]
extra='''<title>Painel do Cidadão</title>
<meta name="description" content="Como estão o Brasil, os 27 estados, as 5.571 cidades e o Congresso, em linguagem simples e atualizado todo dia.">
<meta property="og:title" content="Painel do Cidadão">
<meta property="og:description" content="Como estão o Brasil, seu estado, sua cidade e o Congresso, em linguagem simples.">
<meta property="og:url" content="https://paineldocidadao.com.br/">
<meta name="theme-color" content="#ffffff">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%23111'/%3E%3Cpath d='M8 22V14M14 22V9M20 22V16M26 22V12' stroke='%23fff' stroke-width='3' stroke-linecap='round'/%3E%3C/svg%3E">
'''
out=src.replace('<!doctype html><html>','<!doctype html><html lang="pt-BR">',1)
out=out.replace('<meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover">','<meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover">\n'+extra,1)
out=out.replace('<body>\n<title>Painel do Cidadão</title>\n','<body>\n',1)
assert out.count('<title>')==1, out.count('<title>')
# Estatísticas de visitas (GoatCounter, sem cookies) — só no domínio próprio; conta também as abas (#brasil, #pr...)
gc='''<script>window.goatcounter={path:function(p){return location.pathname+(location.hash&&location.hash!=="#brasil"?location.hash:"")}};
addEventListener("hashchange",function(){if(window.goatcounter&&window.goatcounter.count)window.goatcounter.count({path:location.pathname+(location.hash&&location.hash!=="#brasil"?location.hash:"")})});</script>
<script data-goatcounter="https://paineldocidadao.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
'''
i=out.rindex('</body>'); out=out[:i]+gc+out[i:]
assert out.count('data-goatcounter=')==1
open(dst,'w').write(out)
