<h1 align="center">Monitor.py </h1>
<p align="center">
<img loading="lazy" src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>
</p>


## Descrição do Projeto
<p align="center">Este código é um script de monitoramento de rede escrito em Python que usa a biblioteca Scapy para capturar e analisar o tráfego HTTP. Aqui está uma descrição técnica do que o código faz:</p>

Importação de módulos: O script começa importando vários módulos Python necessários, incluindo os, platform, subprocess e vários módulos do pacote scapy.

Definição de variáveis globais: Em seguida, ele define um dicionário global websites_accessed para armazenar as URLs acessadas por cada dispositivo na rede.

Função ping: Esta função verifica a disponibilidade de um host na rede usando o comando ping. Ela usa o módulo subprocess para executar o comando ping e retorna True se o host estiver disponível e False caso contrário.

Função capture_http_traffic: Esta função é usada para capturar e analisar o tráfego HTTP. Ela é chamada para cada pacote que corresponde ao filtro definido na função sniff. Se o pacote contém uma solicitação HTTP, a função extrai o endereço IP de origem e a URL acessada e armazena essas informações no dicionário websites_accessed.

Monitoramento de tráfego HTTP: O script inicia o monitoramento do tráfego HTTP usando a função sniff do Scapy. Ele configura a função para chamar capture_http_traffic para cada pacote que corresponde ao filtro “tcp port 80 or tcp port 443”.
Verificação de disponibilidade de hosts: O script verifica a disponibilidade de cada host na lista hosts usando a função ping. Para cada host que está online, ele imprime as URLs acessadas pelo host.

Função start_traffic_capture: Esta função inicia a captura de tráfego de rede em tempo real, chamando a função sniff com um filtro para capturar apenas o tráfego na porta TCP 80.

Impressão de websites acessados: Por fim, o script imprime as URLs acessadas por cada dispositivo na rede.
Em resumo, este script monitora o tráfego HTTP na rede, registra as URLs acessadas por cada dispositivo e verifica periodicamente a disponibilidade dos hosts. Ele pode ser útil para monitorar a atividade da rede em um ambiente de rede local.
<h1 align="center">Monitor.py </h1>
<p align="center">
<img loading="lazy" src="http://img.shields.io/static/v1?label=Python&message=Scapy&color=BLUE&style=for-the-badge"/>
</p>


MIT License

Copyright (c) <2024>  <kali0>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
<p align="center">
<img loading="lazy" src="http://img.shields.io/static/v1?label=License&message=MIT&color=GREEN&style=for-the-badge"/>
</p>


