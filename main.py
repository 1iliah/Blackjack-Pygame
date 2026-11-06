import pygame


from cartes import creer_paquet


from jetons import ajouter_a_mise
from jetons import mise_valide
from jetons import partie_terminee


from split import split_possible
from split import effectuer_split


from regles import calculer_score
from regles import terminer_manche


from affichage import afficher_carte
from affichage import afficher_dos_carte


from affichage_jetons import afficher_jetons
from affichage_jetons import detecter_jeton


from interface import LARGEUR
from interface import HAUTEUR
from interface import BLANC

from interface import creer_polices
from interface import obtenir_action_clavier
from interface import obtenir_action_souris
from interface import dessiner_interface


# --------------------------------------------------
# INITIALISATION DE PYGAME
# --------------------------------------------------

pygame.init()


fenetre = pygame.display.set_mode(
    (
        LARGEUR,
        HAUTEUR
    )
)


pygame.display.set_caption(
    "Table de Blackjack"
)


# --------------------------------------------------
# POLICES
# --------------------------------------------------

(
    police_titre,
    police_texte,
    police_info
) = creer_polices()


# --------------------------------------------------
# VARIABLES DE LA PARTIE
# --------------------------------------------------

paquet = []


main_joueur = []


main_croupier = []


mains_joueur = []


mises_joueur = []


main_actuelle = 0


split_actif = False


partie_en_cours = False


croupier_visible = False


message_info = (
    "Choisissez votre mise. "
    "Minimum : 25 jetons."
)


# --------------------------------------------------
# ARGENT
# --------------------------------------------------

jetons = 500


mise = 0


# --------------------------------------------------
# BOUCLE PRINCIPALE
# --------------------------------------------------

jeu_en_cours = True


while jeu_en_cours:


    action = None


    # --------------------------------------------------
    # ÉVÉNEMENTS
    # --------------------------------------------------

    for evenement in pygame.event.get():


        # --------------------------------------------------
        # FERMER LE JEU
        # --------------------------------------------------

        if evenement.type == pygame.QUIT:

            jeu_en_cours = False


        # --------------------------------------------------
        # CLAVIER
        # --------------------------------------------------

        elif evenement.type == pygame.KEYDOWN:


            action_clavier = obtenir_action_clavier(
                evenement.key
            )


            if action_clavier is not None:

                action = action_clavier


        # --------------------------------------------------
        # SOURIS
        # --------------------------------------------------

        elif evenement.type == pygame.MOUSEBUTTONDOWN:


            # --------------------------------------------------
            # CHOISIR UN JETON
            # --------------------------------------------------

            if not partie_en_cours:


                valeur_jeton = detecter_jeton(
                    evenement.pos
                )


                if valeur_jeton is not None:


                    # Si le joueur n'a même plus
                    # 25 jetons au total

                    if partie_terminee(
                        jetons + mise
                    ):

                        message_info = (
                            "Vous avez perdu ! "
                            "Vous n'avez plus assez de jetons."
                        )


                    else:

                        ancienne_mise = mise


                        jetons, mise = ajouter_a_mise(
                            jetons,
                            mise,
                            valeur_jeton
                        )


                        if mise > ancienne_mise:

                            message_info = (
                                "Mise actuelle : "
                                + str(mise)
                                + " jetons."
                            )


                        else:

                            message_info = (
                                "Vous n'avez pas assez "
                                "de jetons pour ajouter ce jeton."
                            )


                    continue


            # --------------------------------------------------
            # AUTRES BOUTONS
            # --------------------------------------------------

            action_souris = obtenir_action_souris(
                evenement.pos
            )


            if action_souris is not None:

                action = action_souris


    # --------------------------------------------------
    # DISTRIBUER
    # --------------------------------------------------

    if action == "distribuer":


        # Plus assez d'argent du tout

        if partie_terminee(
            jetons + mise
        ):

            message_info = (
                "Vous avez perdu ! "
                "Vous n'avez plus assez de jetons."
            )


        # Partie déjà en cours

        elif partie_en_cours:

            message_info = (
                "Terminez d'abord la partie en cours."
            )


        # Mise insuffisante

        elif not mise_valide(
            mise
        ):

            message_info = (
                "La mise minimum est de 25 jetons."
            )


        else:

            # --------------------------------------------------
            # NOUVEAU PAQUET
            # --------------------------------------------------

            paquet = creer_paquet()


            main_joueur = []


            main_croupier = []


            # --------------------------------------------------
            # DEUX CARTES JOUEUR
            # --------------------------------------------------

            main_joueur.append(
                paquet.pop()
            )


            main_joueur.append(
                paquet.pop()
            )


            # --------------------------------------------------
            # DEUX CARTES CROUPIER
            # --------------------------------------------------

            main_croupier.append(
                paquet.pop()
            )


            main_croupier.append(
                paquet.pop()
            )


            # --------------------------------------------------
            # INITIALISATION DES MAINS
            # --------------------------------------------------

            mains_joueur = [
                main_joueur
            ]


            mises_joueur = [
                mise
            ]


            main_actuelle = 0


            split_actif = False


            partie_en_cours = True


            croupier_visible = False


            message_info = (
                "À vous : "
                "T = tirer | "
                "R = rester | "
                "S = split"
            )


            # --------------------------------------------------
            # SCORES DE DÉPART
            # --------------------------------------------------

            score_joueur = calculer_score(
                main_joueur
            )


            score_croupier = calculer_score(
                main_croupier
            )


            # --------------------------------------------------
            # BLACKJACK DÈS LE DÉPART
            # --------------------------------------------------

            if (
                score_joueur == 21
                or score_croupier == 21
            ):


                croupier_visible = True


                partie_en_cours = False


                jetons, message_info = terminer_manche(
                    paquet,
                    main_croupier,
                    mains_joueur,
                    mises_joueur,
                    jetons
                )


                # La manche est terminée :
                # nouvelle mise à choisir.

                mise = 0


                if partie_terminee(
                    jetons
                ):

                    message_info = (
                        "Vous avez perdu ! "
                        "Vous n'avez plus assez de jetons."
                    )


                else:

                    message_info += (
                        " | Choisissez votre prochaine mise."
                    )


    # --------------------------------------------------
    # SPLIT
    # --------------------------------------------------

    elif (
        action == "split"
        and partie_en_cours
    ):


        # Un seul split pour l'instant

        if split_actif:

            message_info = (
                "Vous avez déjà effectué un split."
            )


        # Vérifier les cartes

        elif not split_possible(
            main_joueur
        ):

            message_info = (
                "Split impossible : "
                "les deux cartes doivent être identiques."
            )


        # Il faut une deuxième mise identique

        elif jetons < mise:

            message_info = (
                "Vous n'avez pas assez de jetons "
                "pour effectuer un split."
            )


        else:

            # Retirer la deuxième mise
            # du solde.

            jetons -= mise


            mains_joueur = effectuer_split(
                main_joueur,
                paquet
            )


            mises_joueur = [
                mise,
                mise
            ]


            split_actif = True


            main_actuelle = 0


            main_joueur = mains_joueur[
                main_actuelle
            ]


            message_info = (
                "Split effectué ! "
                "Vous jouez la main 1."
            )


    # --------------------------------------------------
    # TIRER
    # --------------------------------------------------

    elif (
        action == "tirer"
        and partie_en_cours
    ):


        nouvelle_carte = paquet.pop()


        main_joueur.append(
            nouvelle_carte
        )


        score_joueur = calculer_score(
            main_joueur
        )


        message_info = (
            "Vous avez tiré : "
            + nouvelle_carte[0]
            + " de "
            + nouvelle_carte[1].strip()
        )


        # --------------------------------------------------
        # DÉPASSEMENT DE 21
        # --------------------------------------------------

        if score_joueur > 21:


            # Première main après split

            if (
                split_actif
                and main_actuelle == 0
            ):


                main_actuelle = 1


                main_joueur = mains_joueur[
                    main_actuelle
                ]


                message_info = (
                    "Main 1 dépasse 21. "
                    "Vous jouez maintenant la main 2."
                )


            else:

                # Toutes les mains sont terminées

                croupier_visible = True


                partie_en_cours = False


                jetons, message_info = terminer_manche(
                    paquet,
                    main_croupier,
                    mains_joueur,
                    mises_joueur,
                    jetons
                )


                mise = 0


                if partie_terminee(
                    jetons
                ):

                    message_info = (
                        "Vous avez perdu ! "
                        "Vous n'avez plus assez de jetons."
                    )


                else:

                    message_info += (
                        " | Choisissez votre prochaine mise."
                    )


        # --------------------------------------------------
        # SCORE = 21
        # --------------------------------------------------

        elif score_joueur == 21:

            message_info = (
                "Vous avez 21 ! "
                "Appuyez sur R pour rester."
            )


    # --------------------------------------------------
    # RESTER
    # --------------------------------------------------

    elif (
        action == "rester"
        and partie_en_cours
    ):


        # Première main après split

        if (
            split_actif
            and main_actuelle == 0
        ):


            main_actuelle = 1


            main_joueur = mains_joueur[
                main_actuelle
            ]


            message_info = (
                "Main 1 terminée. "
                "Vous jouez maintenant la main 2."
            )


        else:

            # Toutes les mains sont terminées

            croupier_visible = True


            partie_en_cours = False


            jetons, message_info = terminer_manche(
                paquet,
                main_croupier,
                mains_joueur,
                mises_joueur,
                jetons
            )


            mise = 0


            if partie_terminee(
                jetons
            ):

                message_info = (
                    "Vous avez perdu ! "
                    "Vous n'avez plus assez de jetons."
                )


            else:

                message_info += (
                    " | Choisissez votre prochaine mise."
                )


    # --------------------------------------------------
    # NOM DE LA MAIN AFFICHÉE
    # --------------------------------------------------

    if (
        split_actif
        and partie_en_cours
    ):

        nom_main = (
            "Cartes du joueur - Main "
            + str(main_actuelle + 1)
        )


    else:

        nom_main = (
            "Cartes du joueur"
        )


    # --------------------------------------------------
    # MISE AFFICHÉE
    # --------------------------------------------------

    if (
        split_actif
        and partie_en_cours
    ):

        mise_affichee = sum(
            mises_joueur
        )


    else:

        mise_affichee = mise


    # --------------------------------------------------
    # INTERFACE
    # --------------------------------------------------

    dessiner_interface(
        fenetre,
        police_titre,
        police_texte,
        police_info,
        jetons,
        mise_affichee,
        message_info,
        nom_main
    )


    # --------------------------------------------------
    # JETONS GRAPHIQUES
    # --------------------------------------------------

    afficher_jetons(
        fenetre
    )


    # --------------------------------------------------
    # CARTES DU CROUPIER
    # --------------------------------------------------

    for i, carte in enumerate(
        main_croupier
    ):


        x = (
            150
            + i * 105
        )


        y = 125


        if (
            i == 1
            and not croupier_visible
        ):


            afficher_dos_carte(
                fenetre,
                x,
                y
            )


        else:

            afficher_carte(
                fenetre,
                carte,
                x,
                y
            )


    # --------------------------------------------------
    # SCORE DU CROUPIER
    # --------------------------------------------------

    if len(
        main_croupier
    ) > 0:


        if croupier_visible:


            score_croupier = calculer_score(
                main_croupier
            )


            texte_score_croupier = police_texte.render(
                "Score : "
                + str(score_croupier),
                True,
                BLANC
            )


        else:

            texte_score_croupier = police_texte.render(
                "Score : ?",
                True,
                BLANC
            )


        fenetre.blit(
            texte_score_croupier,
            (750, 95)
        )


    # --------------------------------------------------
    # CARTES DU JOUEUR
    # --------------------------------------------------

    for i, carte in enumerate(
        main_joueur
    ):


        x = (
            150
            + i * 105
        )


        y = 365


        afficher_carte(
            fenetre,
            carte,
            x,
            y
        )


    # --------------------------------------------------
    # SCORE DU JOUEUR
    # --------------------------------------------------

    if len(
        main_joueur
    ) > 0:


        score_joueur = calculer_score(
            main_joueur
        )


        texte_score_joueur = police_texte.render(
            "Score : "
            + str(score_joueur),
            True,
            BLANC
        )


        fenetre.blit(
            texte_score_joueur,
            (750, 335)
        )


    # --------------------------------------------------
    # ACTUALISER L'ÉCRAN
    # --------------------------------------------------

    pygame.display.update()


# --------------------------------------------------
# FERMER PYGAME
# --------------------------------------------------

pygame.quit()
