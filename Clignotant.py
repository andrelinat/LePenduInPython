while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:  #si un evenement qui est actionner
            continuer = 0       #on met 0 a la valeur de continuer
        #action sur le bouton gauche de la souris
        if event.type == MOUSEBUTTONUP and event.button == 1 and note.collidepoint(event.pos[0], event.pos[1]) and cadenas == 1 and cli == 0:
            while cli == 0:
                pygame.display.update(fenetre.blit(bouton, (200, 200)))
                time.sleep(0.5)
                pygame.display.update(fenetre.blit(boutonbis, (200, 200)))
                time.sleep(0.5)
                if pygame.event.wait().type == pygame.MOUSEBUTTONDOWN:
                    cli = 1
            pygame.display.update(fenetre.blit(bouton, (300, 300)))
 
        pygame.display.flip()