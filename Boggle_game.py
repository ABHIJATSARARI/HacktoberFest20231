def dfs(board, s, i, j, n, m, idx):
	if i < 0 or i >= n or j < 0 or j >= m:
		return False
	if s[idx] != board[i][j]:
		return False
	if idx == len(s) - 1:
		return True
	temp = board[i][j]
	board[i][j] = '*'
	a = dfs(board, s, i, j+1, n, m, idx+1)
	b = dfs(board, s, i, j-1, n, m, idx+1)
	c = dfs(board, s, i+1, j, n, m, idx+1)
	d = dfs(board, s, i-1, j, n, m, idx+1)
	e = dfs(board, s, i+1, j+1, n, m, idx+1)
	f = dfs(board, s, i-1, j+1, n, m, idx+1)
	g = dfs(board, s, i+1, j-1, n, m, idx+1)
	h = dfs(board, s, i-1, j-1, n, m, idx+1)
	board[i][j] = temp
	return a or b or c or e or f or g or h or d

def wordBoggle(board, dictionary):
	n = len(board)
	m = len(board[0])
	store = set()
	
	#	 Let the given dictionary be following
	for word in dictionary:
		for i in range(n):
			for j in range(m):
				if dfs(board, word, i, j, n, m, 0):
					store.add(word)
	for word in store:
		print(word)

boggle = [['G', 'I', 'Z'],
		['U', 'E', 'K'],
		['Q', 'S', 'E']]
dictionary = ["GEEKS", "FOR", "QUIZ", "GO"]
print("Following words of dictionary are present:")
wordBoggle(boggle, dictionary)

# This code is contributed by vikramshirsath177
