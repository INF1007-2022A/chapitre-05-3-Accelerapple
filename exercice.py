#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def get_num_letters(text):
	count = 0
	for letter in text:
		if letter.isalnum():
			count += 1
	return count

def get_word_length_histogram(text):
	nbr_lettre_par_mot = []
	output = []
	mots = text.split(" ")
	for word in mots:
		nbr_lettre = get_num_letters(word)
		nbr_lettre_par_mot.append(nbr_lettre)

	maximum = max(nbr_lettre_par_mot)
	for quantite in range(maximum+1):
		nbr_mot_n_lettre = nbr_lettre_par_mot.count(quantite)
		output.append(nbr_mot_n_lettre)

	return output

def format_histogram(histogram):
	ROW_CHAR = "*"
	espace = " "
	output = ""

	maximum = len(histogram)-1
	taille_carac_max = len(str(maximum))

	for ligne in range(1, len(histogram)):
		chiffre = str(ligne)
		output += (espace*(taille_carac_max-len(chiffre)) + chiffre + " " + histogram[ligne]*ROW_CHAR + "\n")

	return output

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"
	espace = " "
	output = ""

	hauteur_max = max(histogram)

	for ligne in range(hauteur_max, 0, -1):
		for colone in range(len(histogram)):
			if histogram[colone] >= ligne:
				output += BLOCK_CHAR
			else:
				output += espace

		output += "\n"

	output += (LINE_CHAR*len(histogram))

	return output


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
