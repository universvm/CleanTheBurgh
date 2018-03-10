import numpy as np

def constructDataSet():
	# TO DO: loop through all files
	

	buzzfeed_real_files = []
	for i in range(1:92):
		file_name = "BuzzFeed_Real_" +str(i) + "-Webpage.json"
		buzzfeed_real_files.append()


	buzzfeed_fake_files = []
	for i in range(1:92):
		file_name = "BuzzFeed_Fake_" +str(i) + "-Webpage.json"
		buzzfeed_fake_files.append()


	polifact_real_files = []
	for i in range(1:121):
		file_name = "PolitiFact_Real_" +str(i) + "-Webpage.json"
		polifact_real_files.append()


	polifact_fake_files = []
	for i in range(1:121):
		file_name = "PolitiFact_Fake_" +str(i) + "-Webpage.json"
		polifact_fake_files.append()

	real_files = buzzfeed_real_files + polifact_real_files
	fake_files = buzzfeed_fake_files + polifact_fake_files

	# all words
	all_words = dict()

	for file in real_files:
		array = TODO_to_be_modified_load(file)
		word_freq_dict = TODO_to_be_modified_nlp_process(array)
		all_words = Counter(all_words) + Counter(word_freq_dict)
	
	for file in fake_files:
		array = TODO_to_be_modified_load(file)
		word_freq_dict = TODO_to_be_modified_nlp_process(TODO_to_be_modified_load(array))
		all_words = Counter(all_words) + Counter(word_freq_dict)

	all_words_ls = [*all_words]

	word_index_dict = dict()
	for i in range(0, len(all_words_ls)):
		word_index_dict[all_words_ls[i]] = i

	# num of row = num of docs(news)
	# num of column = num of word features + 1 (url) + 1 (title) + 1 (label fake or real)
	num_of_word_features = len(all_words_ls)
	train_data = np.empty([(91+91+120+120), (num_of_word_features + 3)])
	index_url = num_of_word_features
	index_title = num_of_word_features+1
	index_label = num_of_word_features+2

	counter = 0
	for file in real_files:
		array = TODO_to_be_modified_load(file)
		word_freq_dict = TODO_to_be_modified_nlp_process(TODO_to_be_modified_load(array))
		for word, freq in word_freq_dict:
			train_data[counter][word_index_dict[word]] = freq
			train_data[counter][index_url] = array[2]
			train_data[counter][index_title] = array[0]
			train_data[counter][index_label] = 1
		real_file_counter += 1

	for file in fake_files:
		array = TODO_to_be_modified_load(file)
		word_freq_dict = TODO_to_be_modified_nlp_process(TODO_to_be_modified_load(array))
		for word, freq in word_freq_dict:
			train_data[counter][word_index_dict[word]] = freq
			train_data[counter][index_url] = array[2]
			train_data[counter][index_title] = array[0]
			train_data[counter][index_label] = 0
		real_file_counter += 1

	return train_data