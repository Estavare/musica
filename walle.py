
import re
import random
import discord
from discord.ext import commands



intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix=".",case_insensitive=True, intents=intents)


@bot.event
async def on_ready():
    print(f'Bot está pronto como {bot.user}')
@bot.event
async def on_message(message):
  

  if re.match(r"(\d+)d(\d+)\+(\d+)", message.content) and message.author !=bot.user:
      match = re.match(r"(\d+)d(\d+)\+(\d+)", message.content)
      num_rolls = int(match.group(1))
      dice_faces = int(match.group(2))
      modifier = int(match.group(3))
      rolls = [random.randint(1, dice_faces) for _ in range(num_rolls)]
      total = sum(rolls)
      desisto= (len(str(rolls))*3)+30
      print(desisto)
      rolls.sort(key=int, reverse=True)


      if num_rolls > 1 and desisto<=2000:
        await message.reply(f"Rolando {num_rolls}d{dice_faces}: {rolls} == [{total}] + {modifier} == [{total + modifier}] ")

      elif num_rolls == 1 and desisto<=2000: 
        await message.reply(f"Rolando 1d{dice_faces}: {rolls}  + {modifier} == [{total + modifier}] ")

      else:
        await message.reply('Você passou do limite de cáracteres, tente novamente')
  #d composto soma
  elif re.match(r"(\d+)d(\d+)\-(\d+)", message.content):
    match = re.match(r"(\d+)d(\d+)\-(\d+)", message.content)
    num_rolls = int(match.group(1))
    dice_faces = int(match.group(2))
    modifier = int(match.group(3))
    rolls = [random.randint(1, dice_faces) for _ in range(num_rolls)]
    total = sum(rolls)
    desisto= (len(str(rolls))*3)+30
    print(desisto)
    rolls.sort(key=int, reverse=True)


    if num_rolls > 1 and desisto<=2000:
      await message.reply(f"Rolando {num_rolls}d{dice_faces}: {rolls} == [{total}] - {modifier} == [{total - modifier}] ")

    elif num_rolls == 1 and desisto<=2000: 
      await message.reply(f"Rolando 1d{dice_faces}: {rolls} - {modifier} == [{total - modifier}] ")

    else:
      await message.reply('Você passou do limite de cáracteres, tente novamente')
  #d composto subtracao
  elif re.match(r"(\d+)d(\d+)\*(\d+)", message.content):
    match = re.match(r"(\d+)d(\d+)\*(\d+)", message.content)
    num_rolls = int(match.group(1))
    dice_faces = int(match.group(2))
    modifier = int(match.group(3))
    rolls = [random.randint(1, dice_faces) for _ in range(num_rolls)]
    total = sum(rolls)
    desisto= (len(str(rolls))*3)+30
    print(desisto)
    rolls.sort(key=int, reverse=True)


    if num_rolls > 1 and desisto<=2000:
      await message.reply(f"Rolando {num_rolls}d{dice_faces}: {rolls} == [{total}] * {modifier} == [{total * modifier}] ")

    elif num_rolls == 1 and desisto<=2000: 
      await message.reply(f"Rolando 1d{dice_faces}: {rolls} * {modifier} == [{total * modifier}] ")

    else:
      await message.reply('Você passou do limite de cáracteres, tente novamente')   
  # d composto mult 
  elif re.match(r"(\d+)d(\d+)\/(\d+)", message.content):
      match = re.match(r"(\d+)d(\d+)\/(\d+)", message.content)
      num_rolls = int(match.group(1))
      dice_faces = int(match.group(2))
      modifier = int(match.group(3))
      rolls = [random.randint(1, dice_faces) for _ in range(num_rolls)]
      total = sum(rolls)
      desisto= (len(str(rolls))*3)+30
      print(desisto)
      rolls.sort(key=int, reverse=True)


      if num_rolls > 1 and desisto<=2000:
        await message.reply(f"Rolando {num_rolls}d{dice_faces}: {rolls} == [{total}] / {modifier} == [{total / modifier}] ")

      elif num_rolls == 1 and desisto<=2000: 
        await message.reply(f"Rolando 1d{dice_faces}: {rolls} / {modifier} == [{total / modifier}] ")

      else:
        await message.reply('Você passou do limite de cáracteres, tente novamente')
  #d composto divisão
  elif re.match(r"(\d+)d(\d+)\^(\d+)", message.content):
      match = re.match(r"(\d+)d(\d+)\^(\d+)", message.content)
      num_rolls = int(match.group(1))
      dice_faces = int(match.group(2))
      modifier = int(match.group(3))
      rolls = [random.randint(1, dice_faces) for _ in range(num_rolls)]
      total = sum(rolls)
      desisto= (len(str(rolls))*3)+30
      print(desisto)


      if num_rolls > 1 and desisto<=2000:
        await message.channel.send(f"Rolando {num_rolls}d{dice_faces}: {rolls} == [{total}] ^ {modifier} == [{pow(total,modifier)}] ")

      elif num_rolls == 1 and desisto<=2000: 
        await message.reply(f"Rolando 1d{dice_faces}: {rolls} ^ {modifier} == [{pow(total,modifier)}] ")

      else:
        await message.reply('Você passou do limite de cáracteres, tente novamente')
  #d composto elevado
  elif re.match(r"(\d+)d(\d+)", message.content):

        match = re.match(r"(\d+)d(\d+)", message.content)
        num_rolls = int(match.group(1))
        dice_faces = int(match.group(2))
        rolls = [random.randint(1, dice_faces) for _ in range(num_rolls)]
        total = sum(rolls)
        desisto= (len(str(rolls))*3)+30
        print(desisto)
        rolls.sort(key=int, reverse=True)


        if num_rolls > 1 and desisto<= 2000:
          await message.reply(f"Rolando {num_rolls}d{dice_faces}: {rolls} == [{total}] ")

        elif num_rolls == 1 and desisto<=2000: 
          await message.reply(f"Rolando 1d{dice_faces}: {rolls}")

        else:
          await message.reply('Você passou do limite de cáracteres, tente novamente')
  #d composto
  elif re.match(r"d(\d+)\+(\d)", message.content):
        match = re.match(r"d(\d+)\+(\d)", message.content)
        print(match)  
        dice_faces = int(match.group(1))
        modifier = int(match.group(2))
        rolls = [random.randint(1, dice_faces)]
        desisto= (len(str(rolls))*3)+30
        total= sum(rolls)
        rolls.sort(key=int, reverse=True)

        if  desisto<=2000:
          await message.reply(f"Rolando 1d{dice_faces}: [{rolls}] + {modifier} == [{total + modifier}] ")

        else:
          await message.reply('Você passou do limite de cáracteres, tente novamente')
  #d simples soma
  elif re.match(r"d(\d+)\-(\d)", message.content):
      match = re.match(r"d(\d+)\-(\d)", message.content)
      print(match)  
      dice_faces = int(match.group(1))
      modifier = int(match.group(2))
      rolls = [random.randint(1, dice_faces)]
      desisto= (len(str(rolls))*3)+30
      total= sum(rolls)
      rolls.sort(key=int, reverse=True)

      if  desisto<=2000:
          await message.reply(f"Rolando 1d{dice_faces}: [{rolls}] - {modifier} == [{total - modifier}] ")

      else:
        await message.reply('Você passou do limite de cáracteres, tente novamente')
  #d simples subtração
  elif re.match(r"d(\d+)\*(\d)", message.content):
      match = re.match(r"d(\d+)\*(\d)", message.content)
      print(match)  
      dice_faces = int(match.group(1))
      modifier = int(match.group(2))
      rolls = [random.randint(1, dice_faces)]
      desisto= (len(str(rolls))*3)+30
      total= sum(rolls)
      rolls.sort(key=int, reverse=True)

      if  desisto<=2000:
        await message.reply(f"Rolando 1d{dice_faces}: [{rolls}] * {modifier} == [{total * modifier}] ")

      else:
        await message.reply('Você passou do limite de cáracteres, tente novamente')
  #d simples multiplicação
  elif re.match(r"d(\d+)\/(\d)", message.content):
      match = re.match(r"d(\d+)\/(\d)", message.content)
      print(match)  
      dice_faces = int(match.group(1))
      modifier = int(match.group(2))
      rolls = [random.randint(1, dice_faces)]
      desisto= (len(str(rolls))*3)+30
      total= sum(rolls)
      rolls.sort(key=int, reverse=True)

      if  desisto<=2000:
        await message.reply(f"Rolando 1d{dice_faces}: [{rolls}] / {modifier} == [{total / modifier}] ")

      else:
        await message.reply('Você passou do limite de cáracteres, tente novamente')
  #d simples divisão
  elif re.match(r"d(\d+)\^(\d)", message.content):
      match = re.match(r"d(\d+)\^(\d)", message.content)
      print(match)  
      dice_faces = int(match.group(1))
      modifier = int(match.group(2))
      rolls = [random.randint(1, dice_faces)]
      desisto= (len(str(rolls))*3)+30
      total= sum(rolls)
      rolls.sort(key=int, reverse=True)

      if  desisto<=2000:
        await message.reply(f"Rolando 1d{dice_faces}: [{rolls}] ^ {modifier} == [{pow(total,modifier)}] ")

      else:
        await message.reply('Você passou do limite de cáracteres, tente novamente')
  #d simples elevado
  elif re.match(r"d(\d+)", message.content):
        match = re.match(r"d(\d+)", message.content)
        print(match)  
        dice_faces = int(match.group(1))
        rolls = [random.randint(1, dice_faces)]
        desisto= (len(str(rolls))*3)+30
        rolls.sort(key=int, reverse=True)

        if  desisto<=2000:
          await message.reply(f"Rolando 1d{dice_faces}: {rolls}")

        else:
          await message.reply('Você passou do limite de cáracteres, tente novamente')
#d simples
#dados






  listas = ["1 - O efeito falha e a ação é perdida. Pontos de feitiço ou espaços de feitiço também são perdidos.",
    "2 - Você é tratado como se tivesse a desvantagem Conjuração Verbal até completar um descanso longo.",
    "3 - Você é tratado como se tivesse a desvantagem Conjuração Drenadora até completar um descanso longo.",
    "4 - Por 1 minuto, todos os feitiços e efeitos de esfera lançados a até 9 metros de você (incluindo o seu) são tratados como se o bônus de proficiência do conjurador fosse reduzido em um valor igual ao seu bônus de proficiência.",
    '5 - Todas as criaturas a até 9 metros de você ganham imunidade aos efeitos mágicos de todas as esferas que você não possui por 1 minuto.',
    '6 - Todas as criaturas dentro de 9 metros devem ser bem-sucedidas em um teste de resistência de Sabedoria ou terão seu bônus de proficiência reduzido a 0 por 1 minuto.',
    '7 - Uma criatura de sua escolha a até 90 metros é tratada como se tivesse a desvantagem Conjuração de Drenagem até completar um descanso longo.',
    '8 - Por 1 minuto você deixa para trás um rastro de chamas brilhantes. Qualquer criatura que passe por um espaço que você estava no turno anterior sofre 1d10 de dano de fogo. Uma criatura só pode sofrer este dano uma vez por turno.',
    '9 - Você altera permanentemente a cor para um tom aleatório. Jogue 1d6 para determinar a cor: 1: azul, 2: verde, 3: vermelho, 4: amarelo, 5: rosa, 6: sua escolha.',
    '10 - Por 1 minuto, todos os seus efeitos de esfera mágica são tratados como se suas jogadas de dano fossem sempre seu valor máximo.',
    '11 - Seus braços e pernas são substituídos por tentáculos por 1 minuto. Esses tentáculos não podem segurar nada ou fornecer componentes somáticos, e seu deslocamento base se torna 3 metros e você ganha um deslocamento de escalada de 6 metros. Seus tentáculos são considerados armas simples que causam 1d4 de dano de concussão e possuem a propriedade alcance.',
    '12 - Todas as criaturas a até 36 metros de você devem ser bem-sucedidas em um teste de resistência de Destreza ou cairão no chão. Em vez disso, criaturas voadoras caem 15 metros.',
    '13 - Invertebrados mortos próximos de tamanho Minúsculo e menores animam como mortos-vivos e seguem você por 1 hora. Seu ruído impõe desvantagem em testes de Furtividade.',
    '14 - Uma criatura de sua escolha a até 90 metros é tratada como se tivesse a desvantagem Conjuração Somática até completar um descanso longo.',
    '15 - Por 1 minuto, todos os efeitos de esfera lançados por você têm qualquer dado de dano rolado tratado como tendo rolado seu valor mínimo.',
    '16 - Sempre que sofrer dano, você ganha resistência a esse tipo de dano até o final do seu próximo turno ou até sofrer um tipo diferente de dano. Este efeito dura até você completar um longo descanso.',
   '17 - Todas as criaturas a até 9 metros de você são atingidas por um raio, sofrendo 1d6 de dano de raio. Um teste de resistência de Destreza bem-sucedido nega este dano. O dano de raio aumenta em 1d6 no 5º nível (2d6), 11º nível (3d6) e 17º nível (4d6).',
    '18 - O efeito é lançado sem nenhuma ação necessária.',
    '19 - Você fica extremamente faminto e deve ter sucesso em um teste de resistência de Constituição a cada hora ou será compelido a comer o equivalente a um dia de comida durante aquela hora. Deixar de fazer isso inflige 1 nível de exaustão (até um máximo de nível 5). Um teste bem-sucedido termina este efeito.',
    '20 - O efeito é lançado como uma ação bônus, a menos que seu tempo de lançamento seja menor.',
    '21 - Todas as criaturas a até 9 metros de você no momento deste evento ficam amedrontadas por 1 rodada sempre que virem um rato. Este efeito persiste por 1 semana.',
    '22 - Você está impedido até o final do seu próximo turno.',
    '23 - Uma sombra gêmea sua aparece ao lado de você. Este gêmeo possui todas as suas habilidades e equipamentos, embora tenha apenas 1 ponto de vida. Este gêmeo ajuda você por 1 minuto ou até ser reduzido para 0 hp. Nesse momento, o gêmeo e todos os seus equipamentos desaparecem e qualquer efeito mágico não instantâneo que ele criou também desaparece.',
    '24 - Role duas vezes e obtenha ambos os resultados. Ignore quaisquer resultados que exijam novas jogadas. Se ambos os testes forem ignorados, não há efeito.',
    '25 - Por 1 minuto, todos os efeitos de esfera lançados a até 90 metros de você têm qualquer dado de dano rolado tratado como tendo rolado seu valor máximo.',
    '26 - Um menestrel ilusório segue você por 1 hora, cantando alto suas ações.',
    '27 - Sua percepção do tempo diminui, permitindo que você faça duas ações bônus por rodada por 1 minuto.',
    '28 - Você é tratado como se tivesse a desvantagem Conjuração Somática até completar um descanso longo.',
    '29 - Uma criatura aleatória a até 9 metros esquece tudo o que aconteceu nas últimas 24 horas.',
    '30 - Você ganha imunidade a qualquer efeito mágico que seja capaz de criar por 1 minuto.',
    '31 - Sempre que sofrer danos, você ganha vulnerabilidade a esse tipo de dano até o final do seu próximo turno ou até sofrer um tipo diferente de dano. Este efeito dura até você completar um descanso longo.',
    '32 - O custo de pontos de magia do efeito de ativação aumenta em 1. Se você não tiver pontos de magia suficientes, você não poderá realizar ações ou ações bônus até o final do seu próximo turno.',
    '33 - Qualquer alimento carregado por você no momento do lançamento fica infestado de vermes e não é comestível.',
    '34 - Todas as criaturas hostis a até 9 metros de você ganham imunidade a todos os efeitos mágicos de todas as esferas que você não possui por 1 minuto.',
    '35 - Todas as criaturas em um raio de 30 metros são cercadas por uma barreira grande o suficiente para elas ficarem de pé, mas as mantém no lugar. Esta barreira dura 1 minuto ou até ser destruída. Possui 5 pontos de vida.',
    '36 - Você não pode realizar ações bônus por 1 minuto.',
    '37 - Por 1 minuto, todos os efeitos de esfera que requerem uma ação para serem lançados a até 36 metros de você podem ser lançados como uma ação bônus. Você sempre pode optar por usar o tempo de lançamento normal.',
    '38 - Seu corpo se transforma em planta. Você ganha o tipo de criatura planta por 1 hora e fica imune às condições enfeitiçada, assustada e inconsciente, mas todas as suas velocidades de movimento são reduzidas em 3 metros.',
   '39 - Você recebe o benefício Habilidades Capacitadas por 1 hora.',
    '40 - Todas as criaturas a até 9 metros de você ganham imunidade aos efeitos mágicos de todas as esferas que você possui por 1 minuto.',
    '41 - Você é tratado como se tivesse a desvantagem de Conjuração Estendida até fazer um descanso longo.',
    '42 - Você sofre 50% de chance de falha de feitiço por 1 minuto. Qualquer tentativa de lançar um feitiço ou efeito de esfera tem 50% de chance de falhar, perdendo a ação e o espaço de feitiço ou pontos de feitiço.',
    '43 - Por 1 minuto, qualquer efeito de esfera mágica ou feitiço que você conjure com duração diferente de instantânea ou permanente terá sua duração (ou duração máxima) dobrada.',
    '44 - Seu bônus de proficiência é reduzido a 0 por 1 minuto.',
    '45 - Um pilar estacionário de luz brilhante aparece no espaço do alvo (ou no centro da área alvo) e segue o alvo (ou a criatura mais próxima do centro da área alvo, escolha aleatoriamente se várias criaturas são equidistantes), movendo-se em direção a ele a uma taxa de 9 metros por turno no início de seu turno, passando por objetos sólidos na rota mais curta possível. Qualquer criatura que ocupe um espaço com o pilar de luz no início de seu turno fica cega até terminar seu turno fora do espaço do pilar. Este efeito dura 1 minuto. O pilar se estende 6m verticalmente.',
    '46 - Você ganha imunidade aos efeitos mágicos de todas as esferas que não possuir por 10 minutos.',
    '47 - Você ganha a condição invisível por 1 hora ou até realizar uma ação hostil, o que ocorrer primeiro.',
    '48 - Você fica atordoado até o final do seu próximo turno ao receber uma visão da morte violenta mais recente de um humanóide em um raio de 16 quilômetros.',
    '49 - Um goblin por nível aparece a até 9 metros de você. Esses goblins são hostis a todas as criaturas e atacam o mais próximo possível.',
    '50 - Você ganha conhecimento de um Feito de sua escolha de uma esfera usada no efeito de ativação por 1 rodada.',
    '51 - Uma criatura de sua escolha a até 36 metros sofre um aumento de 25% na chance de magia selvagem de todas as magias e efeitos de esfera até completar um descanso curto ou longo.',
    '52 - Um objeto autônomo de tamanho minúsculo por nível a até 9 metros de você se torna animado conforme o Feito Animar Objeto por 1 minuto. Esses objetos são hostis a você e irão prejudicá-lo da melhor maneira possível.',
    '53 - O efeito falha e a ação é perdida. Pontos de feitiço ou espaços de feitiço não são perdidos.',
    '54 - Você sofre desvantagem em testes de habilidade e testes de resistência para seu modificador de habilidade chave até completar um descanso curto ou longo.',
    '55 - Você está envenenado e incapaz de realizar ações ou ações bônus até o final do seu próximo turno.',
    '56 - Uma criatura de sua escolha a até 90 metros ganha a desvantagem Conjuração Verbal, mas não seus benefícios, até completar um descanso longo.',
    '57 - Todas as criaturas hostis a até 90 metros de você encolhem conforme o Feito Mudança de Tamanho da esfera Alteração por 1 hora.',
    '58 - O alvo ou criaturas na área alvo encolhem de acordo com o Feito Mudança de Tamanho da esfera Alteração por um minuto. Isso se acumula com outros efeitos de mudança de tamanho.',
    '59 - Todas as criaturas a até 9 metros de você devem ser bem-sucedidas em um teste de resistência de Destreza ou começarão a cair para cima a uma taxa de 1,5 metros por rodada. Este efeito evita que a criatura caia, mas de outra forma não tem impacto no movimento da criatura naquela rodada, desde que ela tenha uma velocidade de movimento adequada ao seu ambiente (voar se estiver no ar, nadar se estiver debaixo d\'água, cavar se estiver no subsolo). Este efeito dura 1 minuto',
    '60 - Por 1 minuto por nível, todas as criaturas a até 90 metros cantam alto sobre suas ações, como se estivessem em um musical. Isso confere desvantagem em testes de Furtividade, mas não tem impacto em ações ou qualquer outro efeito mecânico.',
    '61 - O custo de pontos de magia do efeito diminui em 1. Se o efeito não requerer nenhum ponto de magia, você ganha 1 ponto de magia temporário que expira no final do seu próximo turno.',
    '62 - Todos os objetos inflamáveis não vigiados a até 9 metros do alvo ou centro da área alvo são incendiados.',
    '63 - Você sofre dano necrótico igual ao seu bônus de proficiência. Este dano não força testes de concentração para lançar ou manter efeitos de esfera ou feitiços.',
    '64 - Você sofre um aumento de 50% na chance de magia selvagem de todos os feitiços e esferas mágicas até seu próximo descanso curto ou longo.',
    '65 - Você ganha o tipo de criatura morto-vivo por 1 hora. Você é imune a dano necrótico e venenoso e à condição envenenado, mas ganha vulnerabilidade a dano radiante.',
    '66 - Por 1 hora, uma criatura de sua escolha a até 9 metros de você no momento em que este resultado é desencadeado ganha o benefício Habilidades Potenciais.',
    '67 - Todas as criaturas tratam todos os quadrados a até 9 metros de você como terreno difícil por 1 minuto.',
    '68 - Uma chuva de faíscas ilumina o ar em um raio de 1 milha, aumentando o nível de luz para um mínimo de luz normal por 1 minuto.',
    '69 - Você recebe 15 de sedução passiva por 1 hora.',
    '70 - Por 1 minuto, você deixa para trás um rastro brilhante de energia positiva. Qualquer criatura que entrar em um quadrado que você esteve no seu turno anterior cura um número de pontos de vida igual ao seu bônus de proficiência. Criaturas do tipo Morto-vivo, em vez disso, recebem uma quantidade igual de dano radiante. Uma criatura só pode ser afetada por esta habilidade uma vez por turno.',
    '71 - Por 1 minuto, todos os efeitos de esfera mágica ou feitiços lançados a até 90 metros de você que tenham uma duração diferente de instantânea ou permanente têm sua duração (ou duração máxima, para efeitos de concentração) dobrada.',
    '72 - Todas as criaturas aliadas a até 9 metros de você ganham imunidade a todos os efeitos mágicos de todas as esferas que você não possui por 1 minuto.',
    '73 - A cada rodada por 1 minuto você retorna ao local onde começou sua rodada anterior. Este efeito funciona mesmo através de limites planares.',
    '74 - Por 1 minuto, você deixa para trás um rastro sombrio de energia negativa. Qualquer criatura que entrar em um espaço que você ocupou no seu turno anterior sofre 1d10 de dano necrótico. Mortos-vivos são curados na mesma quantidade. Uma criatura só pode ser afetada por esta habilidade uma vez por turno.',
    '75 - Por 1 minuto, todos os itens mágicos a até 90 metros de você emitem luz como uma tocha.',
    '76 - Você perde o conhecimento de qualquer um dos Feitos usados no efeito mágico (mas não a esfera base) pela duração do efeito (mínimo 1 minuto).',
    '77 - Seus pontos de vida máximos são reduzidos pelo seu nível até você completar um descanso longo.',
    '78 - Todos os objetos inflamáveis desacompanhados a até 9 metros de você são incendiados.',
    '79 - Por 1 minuto você cai sempre que tenta mover mais da metade de sua velocidade. Se estiver voando, você cai 15 metros.',
    '80 - Você perde o acesso a todas as esferas mágicas usadas no efeito de ativação por 1 minuto.',
    '81 - Conjurar o efeito requer uma ação no seu próximo turno além do tempo normal de conjuração.',
    '82 - Todas as criaturas a até 9 metros de você devem ser bem-sucedidas em um teste de resistência de Destreza ou ficarão enredadas por plantas, rochas movediças, ou gelo conforme apropriado ao ambiente, tornando-os agarrados por 1 minuto.',
    '83 - Todas as criaturas aliadas a até 90 metros de você encolhem para o tamanho Minúsculo por 1 hora.',
    '84 - Você é atingido por um raio uma vez por rodada, causando 1d4 de dano por raio, por um número de rodadas igual ao seu bônus de proficiência.',
    '85 - Por 1 minuto, todos os efeitos de esfera lançados a até 90 metros de você têm qualquer dado de dano rolado tratado como tendo rolado seu valor mínimo.',
    '86 - Todas as superfícies planas dentro de um cubo de 9 metros ao seu redor estão cobertas de objetos pequenos, duros e redondos. Qualquer criatura que tente sair de um quadrado nesta área deve ser bem-sucedida em um teste de resistência de Destreza ou cairá no chão. Esses objetos persistem por 1 minuto. Um quadrado de 1,5 metro pode ser limpo deles com uma ação.',
    '87 - Uma criatura de sua escolha a até 90 metros é tratada como se tivesse a desvantagem Conjuração Viciante até completar um descanso longo.',
    '88 - Todos os queijos a até 90 metros de você explodem inofensivamente, destruindo o queijo.',
    '89 - O custo de pontos de magia do efeito aumenta em 1d4. Se você não tiver pontos de magia suficientes, você ficará atordoado até o final do seu próximo turno.',
    '90 - Role novamente na tabela Truques de Magia Selvagem.',
    '91 - Por 1 hora, objetos não mágicos que você toca envelhecem temporariamente. A comida fica podre, o metal manchado, o pano gasto e puído. Todos os objetos retornam ao seu estado anterior quando este efeito termina.',
    '92 - Penas caem do céu em uma área a 90 metros de você por 1 minuto, tornando a área fortemente obscurecida.',
    '93 - O efeito falha, mas a ação não é perdida. Pontos de magia ou espaços de magia gastos são perdidos.',
    '94 - Por 1 minuto, todas as criaturas a até 9 metros de você são incapazes de obter vantagem ou desvantagem em qualquer teste.',
    '95 - Um celestial ou demônio de uma tendência oposta a sua (para verdadeiro neutro, LG, CG, LE ou CE é selecionado aleatoriamente) da escolha do GM é chamado pelo Feito avançado de Invocação da esfera de Conjuração, aparecendo adjacente a você. Esta criatura tem ND igual ao seu nível e não está vinculada ou controlada de forma alguma.',
    '96 - Seu nível de exaustão aumenta em 1, até um máximo de 5.',
    '97 - Você é tratado como se tivesse a desvantagem Conjuração Viciante até completar um descanso longo.',
    '98 - Você fica atordoado até o final do seu próximo turno.',
    '99 - Por 1 minuto, todos os efeitos de esfera que requerem uma ação para serem lançados a até 36 metros do alvo ou do centro da área alvo podem ser lançados como uma ação bônus. Você sempre pode optar por usar o tempo de lançamento normal.',
    '100 - Uma criatura de sua escolha a até 90 metros ganha a desvantagem de Conjuração Estendida, mas não seus benefícios, até completar um descanso longo.']



  if re.match(r'selvagem (\d+)', message.content):
    match = int(match.group(1))
    await message.reply(listas[match-1])
#feitiços selvagens

  elif re.match("selvagem", message.content):
    variavel1 = random.randint(0, 99)
    await message.reply(listas[variavel1])
#feitiços selvagens




TOKEN = 'DUxMTYwMzc4MzIyMzIxNDkw.YL0O3w.1ctrFZqeqCRrvnKC8MC6iJ_1KDU'
bot.run("ODUxMTYwMzc4MzIyMzIxNDkw.YL0O3w.1ctrFZqeqCRrvnKC8MC6iJ_1KDU")