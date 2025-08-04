# 12 // notes projet CEP

---

mcause : contient l’origine de l’interruption, la nature de l’interruption

mip : la nature de l’interruption qui est *en train d’être* demandé

- bit 7: type d’interruption “timer”
- bit 11: type d’interruption “externe”

mie: masquer ou demasquer, à titre individuel, soit l’interruption du timer, soit l’interruption externe

il y a un composant intermédiaire qui prend en entrée MIP et MIE et, si une demande d’un type d’interruption est faite par mip et elle est demasquée par mie, alors on crée une cause d’interruption dans le prochain coup d’horloge qui arrivera par le signal irq, qui se trouve dans le registre mcause.

mstatus: registre qui permet de masquer et demasquer les interruptions *au niveau global.* deux signaux de commande :

- mstatus_set  (qui permet d’autoriser les interruptions, on va devoir remettre en place lorsqu’on aille faire `mret`)
- mstatus_reset (qui permet d’interdire les interruptions, ce qu’on va mettre en place lorsqu’on va partir en interruption).

mtvec: registre où on met l’adresse du programme de l’interruption. lorsque le mécanisme va se mettre en place, pc prend la valeur de mtvec.

mempc: registre où on met l’adresse courante du programme courant, de manière à la restaurer lorsque je revienne de l’interruption.

---

programme du prof avec les LEDs :

```nasm
	.text
	
	lui x1, %hi(traitant)      # charge mtvec avec l’adresse du traitant
	addi x1, x1, %lo(traitant) # les deux lignes sont équivalentes à li x1,traitant
	csrrw x0, mtvec, x1
	addi x1, x0, 1 << 3        # rend globalemement sensible aux interruptions
	csrrs x0, mstatus, x1      # Machine Interrupt Enable bit (MIE de mstatus) à 1
	addi x1, x0, 1 << 2        # rend sensible à l’interruption des poussoirs dans le PLIC
	lui x2, 0x0c002            # *(0xC002000) = 2
	sw x1, 0(x2)
	addi x1, x0, 0x7ff         # autorise des interruptions venant du PLIC
	addi x1, x1, 1             # bit 11 = 0x800 => 0x7ff + 1, car constante 12 bits signée pour addi
	                           # les deux lignes précédentes étant équivalente à li x1,0x800
	csrrs x0, mie, x1          # Machine Extern Interrupt Enable bit (MEIE de mie) à 1
	addi x2, x0, 0
	
attente:
	beq x2, x0, attente        # tourne tant que x2 vaut 0
	addi x31, x0, 0x5ad        # indique sur pout que l’on a recu et traité l’interruption
	j attente # boucle infinie
	
traitant:
	addi x2, x0, 1             # change x2 pour sortir de la boucle infinie
	lui x3, 0x0c200            # acquitte l’interruption dans le plic
	addi x3, x3, 4             # les deux lignes sont équivalentes à li x3,0x0C200004
	lw x1, 0(x3)               # par lecture de l’adresse 0x0c2000004
	mret                       # on retourne de l’interruption
```

csrrw: `csrrw x0, mtvec, x1`
permet de mettre dans mtvec l’adresse du programme traitant (là où on va sauter)

csrrs:  `addi x1, x0, 1 << 3 // csrrs x0, mstatus, x1`
on va mettre le bit 3 de `x1` à `3` , puis on va simplement passer cette valeur à `mstatus` pour autoriser les interruptions.

csrrs: `addi x1, x0, 0x7FF` - `addi  x1, x1, 1` - `csrrs x0, mie, x1`
met le bit 11 de `mie` à `1`, pour autoriser les interruptions externes (bouton poussoir)

au moment d’appuyer sur le bouton poussoir : `mepc ← pc`, `pc ← mtvec`, et on masque les interruptions. Puis, à la fin du programme traitant, `pc ← mepc`, et on démasque les interruptions (`mstatus[3] ← 1`)

---