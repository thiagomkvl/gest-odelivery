from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Hub de Inteligência Financeira para Delivery")

HTML_CONTENT = """<!DOCTYPE html>
<html lang="pt-BR" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gestão & Precificação para Delivery</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        darkbg: '#0F172A',
                        cardbg: '#1E293B',
                        borderbg: '#334155',
                        brandaccent: '#3B82F6'
                    }
                }
            }
        }
    </script>
</head>
<body class="bg-darkbg text-slate-100 font-sans min-h-screen flex flex-col md:flex-row">

    <!-- Navegação Lateral -->
    <aside class="w-full md:w-64 bg-cardbg border-r border-borderbg p-6 flex flex-col justify-between shrink-0">
        <div>
            <div class="flex items-center space-x-3 mb-8">
                <span class="text-3xl">🍔</span>
                <div>
                    <h1 class="font-bold text-lg leading-tight">Delivery Hub</h1>
                    <p class="text-xs text-slate-400">Inteligência Financeira</p>
                </div>
            </div>

            <nav class="space-y-2">
                <button onclick="switchTab('hub')" id="btn-hub" class="nav-btn w-full text-left px-4 py-3 rounded-lg flex items-center space-x-3 bg-brandaccent text-white font-medium">
                    <span>🏠</span> <span>Início</span>
                </button>
                <button onclick="switchTab('cmv')" id="btn-cmv" class="nav-btn w-full text-left px-4 py-3 rounded-lg flex items-center space-x-3 text-slate-300 hover:bg-slate-800">
                    <span>🧮</span> <span>Calculadora CMV</span>
                </button>
                <button onclick="switchTab('breakeven')" id="btn-breakeven" class="nav-btn w-full text-left px-4 py-3 rounded-lg flex items-center space-x-3 text-slate-300 hover:bg-slate-800">
                    <span>📈</span> <span>Ponto de Equilíbrio</span>
                </button>
                <button onclick="switchTab('dre')" id="btn-dre" class="nav-btn w-full text-left px-4 py-3 rounded-lg flex items-center space-x-3 text-slate-300 hover:bg-slate-800">
                    <span>🩺</span> <span>Raio-X Financeiro</span>
                </button>
                <button onclick="switchTab('curso')" id="btn-curso" class="nav-btn w-full text-left px-4 py-3 rounded-lg flex items-center space-x-3 text-slate-300 hover:bg-slate-800">
                    <span>🎓</span> <span>Mini Curso</span>
                </button>
            </nav>
        </div>
        <div class="mt-8 pt-4 border-t border-borderbg text-xs text-slate-500 text-center">
            Vercel Serverless Build OK
        </div>
    </aside>

    <!-- Conteúdo Principal -->
    <main class="flex-1 p-6 md:p-10 overflow-y-auto">

        <!-- 1. HUB INICIAL -->
        <section id="tab-hub" class="tab-content">
            <h2 class="text-3xl font-bold mb-2">Painel de Controle Financeiro</h2>
            <p class="text-slate-400 mb-8">Aumente sua margem, domine seus custos e precifique com precisão matemática.</p>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div class="bg-cardbg border border-borderbg p-6 rounded-xl hover:border-brandaccent transition cursor-pointer" onclick="switchTab('cmv')">
                    <div class="text-3xl mb-3">🧮</div>
                    <h3 class="text-xl font-bold mb-2">1. Calculadora de CMV</h3>
                    <p class="text-slate-400 text-sm">Monitore o custo dos insumos, analise a ficha técnica por prato e elimine desperdícios.</p>
                </div>
                <div class="bg-cardbg border border-borderbg p-6 rounded-xl hover:border-brandaccent transition cursor-pointer" onclick="switchTab('breakeven')">
                    <div class="text-3xl mb-3">📈</div>
                    <h3 class="text-xl font-bold mb-2">2. Ponto de Equilíbrio</h3>
                    <p class="text-slate-400 text-sm">Descubra o faturamento mínimo diário e mensal necessário para cobrir 100% das despesas.</p>
                </div>
                <div class="bg-cardbg border border-borderbg p-6 rounded-xl hover:border-brandaccent transition cursor-pointer" onclick="switchTab('dre')">
                    <div class="text-3xl mb-3">🩺</div>
                    <h3 class="text-xl font-bold mb-2">3. Raio-X Financeiro</h3>
                    <p class="text-slate-400 text-sm">Diagnóstico DRE Operacional completo. Avalie o impacto das taxas de apps no seu lucro real.</p>
                </div>
                <div class="bg-cardbg border border-borderbg p-6 rounded-xl hover:border-brandaccent transition cursor-pointer" onclick="switchTab('curso')">
                    <div class="text-3xl mb-3">🎓</div>
                    <h3 class="text-xl font-bold mb-2">4. Mini Curso: Precificação</h3>
                    <p class="text-slate-400 text-sm">Aprenda a aplicar o Markup Divisor e substitua fórmulas ultrapassadas de precificação.</p>
                </div>
            </div>
        </section>

        <!-- 2. CALCULADORA CMV -->
        <section id="tab-cmv" class="tab-content hidden">
            <h2 class="text-2xl font-bold mb-6">🧮 Calculadora de CMV</h2>
            <div class="flex space-x-4 mb-6 border-b border-borderbg pb-2">
                <button onclick="switchSubTabCMV('cmv-global')" id="btn-sub-global" class="text-brandaccent font-bold pb-2 border-b-2 border-brandaccent">CMV Global Periódico</button>
                <button onclick="switchSubTabCMV('cmv-ficha')" id="btn-sub-ficha" class="text-slate-400 hover:text-slate-200 font-bold pb-2">Ficha Técnica por Prato</button>
            </div>

            <div id="subtab-cmv-global">
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
                    <div class="bg-cardbg p-6 rounded-xl border border-borderbg space-y-4">
                        <div>
                            <label class="block text-sm text-slate-400 mb-1">Faturamento Bruto Total (R$)</label>
                            <input type="number" id="cmv-fat" value="50000" oninput="calcCMV()" class="w-full bg-slate-900 border border-borderbg rounded p-2.5 text-white">
                        </div>
                        <div>
                            <label class="block text-sm text-slate-400 mb-1">Estoque Inicial (R$)</label>
                            <input type="number" id="cmv-est-ini" value="8000" oninput="calcCMV()" class="w-full bg-slate-900 border border-borderbg rounded p-2.5 text-white">
                        </div>
                        <div>
                            <label class="block text-sm text-slate-400 mb-1">Compras de Insumos no Período (R$)</label>
                            <input type="number" id="cmv-compras" value="17000" oninput="calcCMV()" class="w-full bg-slate-900 border border-borderbg rounded p-2.5 text-white">
                        </div>
                        <div>
                            <label class="block text-sm text-slate-400 mb-1">Estoque Final Contado (R$)</label>
                            <input type="number" id="cmv-est-fin" value="9000" oninput="calcCMV()" class="w-full bg-slate-900 border border-borderbg rounded p-2.5 text-white">
                        </div>
                    </div>

                    <div class="bg-cardbg p-6 rounded-xl border border-borderbg flex flex-col justify-between">
                        <div>
                            <h3 class="text-lg font-bold mb-4">Resultado Operacional</h3>
                            <div class="grid grid-cols-2 gap-4 mb-6">
                                <div class="bg-slate-900 p-4 rounded-lg border border-borderbg">
                                    <span class="text-xs text-slate-400">CMV em Reais</span>
                                    <div id="res-cmv-reais" class="text-2xl font-bold text-red-400">R$ 16.000,00</div>
                                </div>
                                <div class="bg-slate-900 p-4 rounded-lg border border-borderbg">
                                    <span class="text-xs text-slate-400">CMV % Faturamento</span>
                                    <div id="res-cmv-pct" class="text-2xl font-bold text-amber-400">32,00%</div>
                                </div>
                            </div>
                            <div id="cmv-status-box" class="p-4 rounded-lg text-sm font-medium bg-emerald-950 text-emerald-300 border border-emerald-800">
                                🟢 CMV Dentro da faixa ideal para Delivery (28% a 32%).
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div id="subtab-cmv-ficha" class="hidden">
                <div class="bg-cardbg p-6 rounded-xl border border-borderbg space-y-6">
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div>
                            <label class="block text-sm text-slate-400 mb-1">Nome do Prato/Combo</label>
                            <input type="text" id="ficha-nome" value="Burguer Smash Duplo" class="w-full bg-slate-900 border border-borderbg rounded p-2 text-white">
                        </div>
                        <div>
                            <label class="block text-sm text-slate-400 mb-1">Preço de Venda no App (R$)</label>
                            <input type="number" id="ficha-preco" value="35.00" oninput="calcFicha()" class="w-full bg-slate-900 border border-borderbg rounded p-2 text-white">
                        </div>
                    </div>

                    <div>
                        <h4 class="font-bold text-slate-200 mb-3">Insumos & Embalagens</h4>
                        <div class="overflow-x-auto">
                            <table class="w-full text-left text-sm text-slate-300">
                                <thead class="bg-slate-900 text-xs text-slate-400 uppercase">
                                    <tr>
                                        <th class="p-2">Item / Insumo</th>
                                        <th class="p-2 w-28">Qtd</th>
                                        <th class="p-2 w-32">Custo Unit (R$)</th>
                                        <th class="p-2 w-32 text-right">Custo Total</th>
                                    </tr>
                                </thead>
                                <tbody id="ficha-rows" class="divide-y divide-borderbg">
                                    <tr>
                                        <td class="p-2"><input type="text" value="Pão Brioche" class="w-full bg-transparent"></td>
                                        <td class="p-2"><input type="number" value="1" oninput="calcFicha()" class="ficha-qtd w-full bg-slate-900 p-1 rounded"></td>
                                        <td class="p-2"><input type="number" value="1.50" step="0.1" oninput="calcFicha()" class="ficha-custo w-full bg-slate-900 p-1 rounded"></td>
                                        <td class="p-2 text-right ficha-tot font-bold">R$ 1,50</td>
                                    </tr>
                                    <tr>
                                        <td class="p-2"><input type="text" value="Hambúrguer 100g" class="w-full bg-transparent"></td>
                                        <td class="p-2"><input type="number" value="2" oninput="calcFicha()" class="ficha-qtd w-full bg-slate-900 p-1 rounded"></td>
                                        <td class="p-2"><input type="number" value="3.20" step="0.1" oninput="calcFicha()" class="ficha-custo w-full bg-slate-900 p-1 rounded"></td>
                                        <td class="p-2 text-right ficha-tot font-bold">R$ 6,40</td>
                                    </tr>
                                    <tr>
                                        <td class="p-2"><input type="text" value="Queijo Cheddar" class="w-full bg-transparent"></td>
                                        <td class="p-2"><input type="number" value="2" oninput="calcFicha()" class="ficha-qtd w-full bg-slate-900 p-1 rounded"></td>
                                        <td class="p-2"><input type="number" value="0.80" step="0.1" oninput="calcFicha()" class="ficha-custo w-full bg-slate-900 p-1 rounded"></td>
                                        <td class="p-2 text-right ficha-tot font-bold">R$ 1,60</td>
                                    </tr>
                                    <tr>
                                        <td class="p-2"><input type="text" value="Embalagem Burger" class="w-full bg-transparent"></td>
                                        <td class="p-2"><input type="number" value="1" oninput="calcFicha()" class="ficha-qtd w-full bg-slate-900 p-1 rounded"></td>
                                        <td class="p-2"><input type="number" value="1.20" step="0.1" oninput="calcFicha()" class="ficha-custo w-full bg-slate-900 p-1 rounded"></td>
                                        <td class="p-2 text-right ficha-tot font-bold">R$ 1,20</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>

                    <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 pt-4 border-t border-borderbg">
                        <div class="bg-slate-900 p-4 rounded-lg">
                            <span class="text-xs text-slate-400">Custo Total Insumos</span>
                            <div id="ficha-res-custo" class="text-2xl font-bold text-red-400">R$ 10,70</div>
                        </div>
                        <div class="bg-slate-900 p-4 rounded-lg">
                            <span class="text-xs text-slate-400">Preço de Venda</span>
                            <div id="ficha-res-preco" class="text-2xl font-bold text-slate-100">R$ 35,00</div>
                        </div>
                        <div class="bg-slate-900 p-4 rounded-lg">
                            <span class="text-xs text-slate-400">CMV Direto do Item</span>
                            <div id="ficha-res-cmv" class="text-2xl font-bold text-amber-400">30,6%</div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 3. PONTO DE EQUILÍBRIO -->
        <section id="tab-breakeven" class="tab-content hidden">
            <h2 class="text-2xl font-bold mb-6">📈 Ponto de Equilíbrio (Break-even)</h2>
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8">
                <div class="bg-cardbg p-6 rounded-xl border border-borderbg space-y-4">
                    <h3 class="font-bold text-brandaccent">1. Custos Fixos Mensais</h3>
                    <div>
                        <label class="block text-sm text-slate-400 mb-1">Custos Fixos Totais (R$)</label>
                        <input type="number" id="be-fixo" value="15000" oninput="calcBreakEven()" class="w-full bg-slate-900 border border-borderbg rounded p-2.5 text-white">
                    </div>
                    <div>
                        <label class="block text-sm text-slate-400 mb-1">Ticket Médio por Pedido (R$)</label>
                        <input type="number" id="be-ticket" value="45" oninput="calcBreakEven()" class="w-full bg-slate-900 border border-borderbg rounded p-2.5 text-white">
                    </div>
                </div>

                <div class="bg-cardbg p-6 rounded-xl border border-borderbg space-y-4">
                    <h3 class="font-bold text-brandaccent">2. Margem de Contribuição</h3>
                    <div>
                        <label class="block text-sm text-slate-400 mb-1">CMV Médio (%)</label>
                        <input type="number" id="be-cmv" value="32" oninput="calcBreakEven()" class="w-full bg-slate-900 border border-borderbg rounded p-2.5 text-white">
                    </div>
                    <div>
                        <label class="block text-sm text-slate-400 mb-1">Taxas Variáveis Totais (%)</label>
                        <input type="number" id="be-var" value="28" oninput="calcBreakEven()" class="w-full bg-slate-900 border border-borderbg rounded p-2.5 text-white">
                    </div>
                </div>
            </div>

            <div class="bg-cardbg p-6 rounded-xl border border-borderbg">
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-6">
                    <div class="bg-slate-900 p-4 rounded-lg">
                        <span class="text-xs text-slate-400">Margem de Contribuição</span>
                        <div id="be-res-mc" class="text-2xl font-bold text-blue-400">40.0%</div>
                    </div>
                    <div class="bg-slate-900 p-4 rounded-lg">
                        <span class="text-xs text-slate-400">Faturamento Mínimo / Mês</span>
                        <div id="be-res-fat" class="text-2xl font-bold text-emerald-400">R$ 37.500,00</div>
                    </div>
                    <div class="bg-slate-900 p-4 rounded-lg">
                        <span class="text-xs text-slate-400">Pedidos Mínimos / Dia</span>
                        <div id="be-res-pedidos" class="text-2xl font-bold text-amber-400">27.8/dia</div>
                    </div>
                </div>
                <div class="h-64">
                    <canvas id="chartBreakeven"></canvas>
                </div>
            </div>
        </section>

        <!-- 4. RAIO-X FINANCEIRO -->
        <section id="tab-dre" class="tab-content hidden">
            <h2 class="text-2xl font-bold mb-6">🩺 Raio-X Financeiro (DRE Operacional)</h2>
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
                <div class="bg-cardbg p-6 rounded-xl border border-borderbg space-y-4">
                    <h3 class="font-bold text-brandaccent">Entradas de Vendas</h3>
                    <div>
                        <label class="block text-xs text-slate-400 mb-1">Faturamento Bruto Total (R$)</label>
                        <input type="number" id="dre-fat" value="60000" oninput="calcDRE()" class="w-full bg-slate-900 border border-borderbg rounded p-2 text-white">
                    </div>
                    <div>
                        <label class="block text-xs text-slate-400 mb-1">Participação iFood (%)</label>
                        <input type="number" id="dre-ifood-pct" value="60" oninput="calcDRE()" class="w-full bg-slate-900 border border-borderbg rounded p-2 text-white">
                    </div>
                    <div>
                        <label class="block text-xs text-slate-400 mb-1">Taxa Média iFood (%)</label>
                        <input type="number" id="dre-ifood-taxa" value="21.5" oninput="calcDRE()" class="w-full bg-slate-900 border border-borderbg rounded p-2 text-white">
                    </div>
                    <div>
                        <label class="block text-xs text-slate-400 mb-1">CMV %</label>
                        <input type="number" id="dre-cmv" value="32" oninput="calcDRE()" class="w-full bg-slate-900 border border-borderbg rounded p-2 text-white">
                    </div>
                    <div>
                        <label class="block text-xs text-slate-400 mb-1">Custos Fixos Totais (R$)</label>
                        <input type="number" id="dre-fixo" value="14000" oninput="calcDRE()" class="w-full bg-slate-900 border border-borderbg rounded p-2 text-white">
                    </div>
                </div>

                <div class="lg:col-span-2 bg-cardbg p-6 rounded-xl border border-borderbg">
                    <h3 class="font-bold mb-4">Demonstrativo de Resultado</h3>
                    <div class="overflow-x-auto">
                        <table class="w-full text-left text-sm text-slate-300">
                            <thead class="bg-slate-900 text-slate-400 uppercase text-xs">
                                <tr>
                                    <th class="p-3">Indicador DRE</th>
                                    <th class="p-3 text-right">Valor (R$)</th>
                                    <th class="p-3 text-right">% Fat.</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-borderbg">
                                <tr><td class="p-3 font-semibold">1. Faturamento Bruto</td><td id="dre-row-fat" class="p-3 text-right">R$ 60.000,00</td><td class="p-3 text-right">100%</td></tr>
                                <tr><td class="p-3 text-red-400">(-) Taxas e Comissões Apps</td><td id="dre-row-apps" class="p-3 text-right text-red-400">-R$ 7.740,00</td><td id="dre-row-apps-pct" class="p-3 text-right text-red-400">-12.9%</td></tr>
                                <tr><td class="p-3 text-red-400">(-) CMV Insumos</td><td id="dre-row-cmv" class="p-3 text-right text-red-400">-R$ 19.200,00</td><td class="p-3 text-right text-red-400">-32.0%</td></tr>
                                <tr><td class="p-3 text-red-400">(-) Impostos & Cartão (9%)</td><td id="dre-row-imp" class="p-3 text-right text-red-400">-R$ 5.400,00</td><td class="p-3 text-right text-red-400">-9.0%</td></tr>
                                <tr class="bg-slate-900 font-bold"><td class="p-3 text-blue-400">= Margem de Contribuição</td><td id="dre-row-mc" class="p-3 text-right text-blue-400">R$ 27.660,00</td><td id="dre-row-mc-pct" class="p-3 text-right text-blue-400">46.1%</td></tr>
                                <tr><td class="p-3 text-red-400">(-) Custos Fixos Operacionais</td><td id="dre-row-fixo" class="p-3 text-right text-red-400">-R$ 14.000,00</td><td id="dre-row-fixo-pct" class="p-3 text-right text-red-400">-23.3%</td></tr>
                                <tr class="bg-emerald-950 text-emerald-300 font-bold text-base"><td class="p-3">= LUCRO LÍQUIDO OPERACIONAL</td><td id="dre-row-lucro" class="p-3 text-right">R$ 13.660,00</td><td id="dre-row-lucro-pct" class="p-3 text-right">22.8%</td></tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </section>

        <!-- 5. MINI CURSO -->
        <section id="tab-curso" class="tab-content hidden">
            <h2 class="text-2xl font-bold mb-6">🎓 Mini Curso & Simulador de Precificação</h2>
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
                <div class="bg-cardbg p-6 rounded-xl border border-borderbg space-y-4">
                    <h3 class="text-xl font-bold text-brandaccent">Simulador de Markup Divisor</h3>
                    <div>
                        <label class="block text-sm text-slate-400 mb-1">Custo Insumos + Embalagem (R$)</label>
                        <input type="number" id="mk-custo" value="12" oninput="calcMarkup()" class="w-full bg-slate-900 border border-borderbg rounded p-2.5 text-white">
                    </div>
                    <div>
                        <label class="block text-sm text-slate-400 mb-1">Comissão Canal/iFood (%)</label>
                        <input type="number" id="mk-app" value="23" oninput="calcMarkup()" class="w-full bg-slate-900 border border-borderbg rounded p-2.5 text-white">
                    </div>
                    <div>
                        <label class="block text-sm text-slate-400 mb-1">Impostos Simples Nacional (%)</label>
                        <input type="number" id="mk-imp" value="6" oninput="calcMarkup()" class="w-full bg-slate-900 border border-borderbg rounded p-2.5 text-white">
                    </div>
                    <div>
                        <label class="block text-sm text-slate-400 mb-1">Margem Desejada (%)</label>
                        <input type="number" id="mk-lucro" value="35" oninput="calcMarkup()" class="w-full bg-slate-900 border border-borderbg rounded p-2.5 text-white">
                    </div>
                </div>

                <div class="bg-cardbg p-6 rounded-xl border border-borderbg flex flex-col justify-between">
                    <div>
                        <h3 class="text-lg font-bold mb-4">Preço Sugerido de Venda</h3>
                        <div class="bg-slate-900 p-6 rounded-xl border border-borderbg text-center mb-6">
                            <span class="text-xs text-slate-400 uppercase tracking-wider">Preço Final no Cardápio</span>
                            <div id="mk-res-preco" class="text-4xl font-extrabold text-emerald-400 mt-2">R$ 33,33</div>
                        </div>
                        <div class="space-y-2 text-sm text-slate-300">
                            <div class="flex justify-between p-2 bg-slate-900/50 rounded"><span>🔴 App / Marketplace:</span><span id="mk-det-app">R$ 7,67</span></div>
                            <div class="flex justify-between p-2 bg-slate-900/50 rounded"><span>🟡 Insumos / Insumos:</span><span id="mk-det-custo">R$ 12,00</span></div>
                            <div class="flex justify-between p-2 bg-slate-900/50 rounded"><span>🟢 Margem Bruta Retida:</span><span id="mk-det-lucro">R$ 11,67</span></div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

    </main>

    <script>
        function switchTab(tabId) {
            document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
            document.querySelectorAll('.nav-btn').forEach(el => {
                el.classList.remove('bg-brandaccent', 'text-white');
                el.classList.add('text-slate-300');
            });

            document.getElementById('tab-' + tabId).classList.remove('hidden');
            const activeBtn = document.getElementById('btn-' + tabId);
            if(activeBtn) {
                activeBtn.classList.add('bg-brandaccent', 'text-white');
            }

            if(tabId === 'breakeven') calcBreakEven();
        }

        function switchSubTabCMV(subId) {
            document.getElementById('subtab-cmv-global').classList.add('hidden');
            document.getElementById('subtab-cmv-ficha').classList.add('hidden');
            
            document.getElementById('btn-sub-global').classList.remove('text-brandaccent', 'border-b-2', 'border-brandaccent');
            document.getElementById('btn-sub-ficha').classList.remove('text-brandaccent', 'border-b-2', 'border-brandaccent');
            document.getElementById('btn-sub-global').classList.add('text-slate-400');
            document.getElementById('btn-sub-ficha').classList.add('text-slate-400');

            document.getElementById('subtab-' + subId).classList.remove('hidden');
            
            if(subId === 'cmv-global') {
                document.getElementById('btn-sub-global').classList.add('text-brandaccent', 'border-b-2', 'border-brandaccent');
            } else {
                document.getElementById('btn-sub-ficha').classList.add('text-brandaccent', 'border-b-2', 'border-brandaccent');
                calcFicha();
            }
        }

        function calcCMV() {
            const fat = parseFloat(document.getElementById('cmv-fat').value) || 0;
            const ini = parseFloat(document.getElementById('cmv-est-ini').value) || 0;
            const compras = parseFloat(document.getElementById('cmv-compras').value) || 0;
            const fin = parseFloat(document.getElementById('cmv-est-fin').value) || 0;

            const cmvReais = (ini + compras) - fin;
            const cmvPct = fat > 0 ? (cmvReais / fat) * 100 : 0;

            document.getElementById('res-cmv-reais').innerText = 'R$ ' + cmvReais.toLocaleString('pt-BR', {minimumFractionDigits: 2});
            document.getElementById('res-cmv-pct').innerText = cmvPct.toFixed(2) + '%';
        }

        function calcFicha() {
            const precoVenda = parseFloat(document.getElementById('ficha-preco').value) || 1;
            const qtds = document.querySelectorAll('.ficha-qtd');
            const custos = document.querySelectorAll('.ficha-custo');
            const tots = document.querySelectorAll('.ficha-tot');

            let custoTotalSum = 0;

            qtds.forEach((qtdEl, idx) => {
                const q = parseFloat(qtdEl.value) || 0;
                const c = parseFloat(custos[idx].value) || 0;
                const tot = q * c;
                custoTotalSum += tot;
                tots[idx].innerText = 'R$ ' + tot.toFixed(2);
            });

            const cmvPct = (custoTotalSum / precoVenda) * 100;

            document.getElementById('ficha-res-custo').innerText = 'R$ ' + custoTotalSum.toFixed(2);
            document.getElementById('ficha-res-preco').innerText = 'R$ ' + precoVenda.toFixed(2);
            document.getElementById('ficha-res-cmv').innerText = cmvPct.toFixed(1) + '%';
        }

        let chartInstance = null;
        function calcBreakEven() {
            const fixo = parseFloat(document.getElementById('be-fixo').value) || 0;
            const ticket = parseFloat(document.getElementById('be-ticket').value) || 1;
            const cmv = parseFloat(document.getElementById('be-cmv').value) || 0;
            const variaveis = parseFloat(document.getElementById('be-var').value) || 0;

            const mcPct = 100 - (cmv + variaveis);
            const fatMin = mcPct > 0 ? fixo / (mcPct / 100) : 0;
            const pedidosDia = fatMin > 0 ? (fatMin / ticket) / 30 : 0;

            document.getElementById('be-res-mc').innerText = mcPct.toFixed(1) + '%';
            document.getElementById('be-res-fat').innerText = 'R$ ' + fatMin.toLocaleString('pt-BR', {maximumFractionDigits: 0});
            document.getElementById('be-res-pedidos').innerText = pedidosDia.toFixed(1) + '/dia';

            renderChart(fatMin, fixo, mcPct);
        }

        function renderChart(fatMin = 37500, fixo = 15000, mcPct = 40) {
            const ctx = document.getElementById('chartBreakeven').getContext('2d');
            if(chartInstance) chartInstance.destroy();

            const labels = [0, fatMin * 0.5, fatMin, fatMin * 1.5, fatMin * 2];
            const receita = labels;
            const custos = labels.map(f => fixo + (f * (1 - mcPct/100)));

            chartInstance = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels.map(v => 'R$ ' + (v/1000).toFixed(0) + 'k'),
                    datasets: [
                        { label: 'Faturamento', data: receita, borderColor: '#2ecc71', borderWidth: 2 },
                        { label: 'Custos Totais', data: custos, borderColor: '#e74c3c', borderWidth: 2 }
                    ]
                },
                options: { responsive: true, maintainAspectRatio: false }
            });
        }

        function calcDRE() {
            const fat = parseFloat(document.getElementById('dre-fat').value) || 0;
            const ifoodPct = parseFloat(document.getElementById('dre-ifood-pct').value) || 0;
            const ifoodTaxa = parseFloat(document.getElementById('dre-ifood-taxa').value) || 0;
            const cmvPct = parseFloat(document.getElementById('dre-cmv').value) || 0;
            const fixo = parseFloat(document.getElementById('dre-fixo').value) || 0;

            const appsVal = fat * (ifoodPct/100) * (ifoodTaxa/100);
            const cmvVal = fat * (cmvPct/100);
            const impVal = fat * 0.09;
            const mcVal = fat - appsVal - cmvVal - impVal;
            const lucroVal = mcVal - fixo;

            document.getElementById('dre-row-fat').innerText = 'R$ ' + fat.toLocaleString('pt-BR');
            document.getElementById('dre-row-apps').innerText = '-R$ ' + appsVal.toLocaleString('pt-BR');
            document.getElementById('dre-row-cmv').innerText = '-R$ ' + cmvVal.toLocaleString('pt-BR');
            document.getElementById('dre-row-mc').innerText = 'R$ ' + mcVal.toLocaleString('pt-BR');
            document.getElementById('dre-row-lucro').innerText = 'R$ ' + lucroVal.toLocaleString('pt-BR');
            document.getElementById('dre-row-lucro-pct').innerText = fat > 0 ? ((lucroVal/fat)*100).toFixed(1) + '%' : '0%';
        }

        function calcMarkup() {
            const custo = parseFloat(document.getElementById('mk-custo').value) || 0;
            const app = parseFloat(document.getElementById('mk-app').value) || 0;
            const imp = parseFloat(document.getElementById('mk-imp').value) || 0;
            const lucro = parseFloat(document.getElementById('mk-lucro').value) || 0;

            const somaPct = app + imp + lucro;
            if(somaPct < 100) {
                const preco = custo / (1 - (somaPct/100));
                document.getElementById('mk-res-preco').innerText = 'R$ ' + preco.toFixed(2);
                document.getElementById('mk-det-app').innerText = 'R$ ' + (preco * (app/100)).toFixed(2);
                document.getElementById('mk-det-custo').innerText = 'R$ ' + custo.toFixed(2);
                document.getElementById('mk-det-lucro').innerText = 'R$ ' + (preco * (lucro/100)).toFixed(2);
            }
        }

        calcCMV();
        calcDRE();
        calcMarkup();
    </script>
</body>
</html>
"""

@app.get("/{full_path:path}", response_class=HTMLResponse)
async def serve_dashboard(full_path: str = ""):
    return HTMLResponse(content=HTML_CONTENT, status_code=200)
