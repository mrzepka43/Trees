import time
import math
import random
import sys
import threading

sys.setrecursionlimit(10000000)
threading.stack_size(2**26)

# uzyta funkcja sortujaca
def merge_sort(tab):
    halfsize = int(len(tab) / 2)
    if len(tab) == 1:
        return tab
    else:
        left = []
        right = []
        for i in range(halfsize):
            left.append(tab[i])
        for i in range(halfsize, len(tab)):
            right.append(tab[i])

        merge_sort(left)
        merge_sort(right)

        i = 0 #iteracja lewej tablicy
        j = 0 #iteracja prawej tablicy
        k = 0 #iteracja wynikowej tablicy
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                tab[k] = left[i]
                i += 1
                k += 1
            else:
                tab[k] = right[j]
                j += 1
                k += 1
        if i == len(left):
            while j < len(right):
                tab[k] = right[j]
                k += 1
                j += 1
        if j == len(right):
            while i < len(left):
                tab[k] = left[i]
                k += 1
                i += 1
        return tab


# drzewo BST
class BSTTreenode:
    # konstruktor drzewa zawiera wszystkie cechy klasy
    def __init__(self, value, id = 1):
        self.right = None
        self.left = None
        self.id = id
        self.value = value

    # metoda wstawiajaca wezel BST
    def insertnode(self, value):
        if (self.value == None): # jesli wezel nie istnieje to wstaw wartosc
            self.value = value
        if (self.value > value): # jesli istnieje, to porownaj wartosci, jesli jest mniejsza
            if(self.left == None):# i lewy wezel jest wolny
                self.left = BSTTreenode(value, self.id*2) # to wstaw do lewego wezla z id * 2
            else:
                self.left.insertnode(value) # jesli nie powtorz insert dla lewego wezla
        else:
            if (self.right == None): # to samo dla prawego, gdy wartosc jest wieksza lub rowna
                self.right = BSTTreenode(value, (self.id * 2) + 1)
            else:
                self.right.insertnode(value)

# wyszukiwanie najwiekszego elementu
    def greatest(self, path):
        if (self.right == None):
            path.append(self.value)
            print("odwiedzony wezel")
            print(self.value)
            print(path)
            return self.value
        else:
            path.append(self.value)
            print("odwiedzony wezel")
            print(self.value)
            return self.right.greatest(path)

# wyszukiwanie najmniejszego elementu
    def smallest(self):
        if (self.left == None):
            return self.value
        else:
            return self.left.smallest()

    def __del__(self):
        self.right = None
        self.left = None
        self.id = None
        self.value = None

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


# drzewo AVL
class AVLTreenode:
    # konstruktor drzewa zawiera wszystkie cechy klasy
    def __init__(self, value, id = 1):
        self.right = None
        self.left = None
        self.id = id
        self.value = value

    # metoda wstawiajaca wezel AVL
    def insertnode(self, value):
        if (self.value == None): # jesli wezel nie istnieje to wstaw wartosc
            self.value = value
        if (self.value > value): # jesli istnieje, to porownaj wartosci, jesli jest mniejsza
            if(self.left == None):# i lewy wezel jest wolny
                self.left = AVLTreenode(value, self.id*2) # to wstaw do lewego wezla z id * 2
            else:
                self.left.insertnode(value) # jesli nie powtorz insert dla lewego wezla
        else:
            if (self.right == None): # to samo dla prawego, gdy wartosc jest wieksza lub rowna
                self.right = AVLTreenode(value, (self.id * 2) + 1)
            else:
                self.right.insertnode(value)

# wyszukiwanie najwiekszego elementu
    def greatest(self, path):
        if (self.right == None):
            print("odwiedzony wezel")
            print(self.value)
            path.append(self.value)
            print(path)
            return self.value
        else:
            path.append(self.value)
            print("odwiedzony wezel")
            print(self.value)
            return self.right.greatest(path)

# wyszukiwanie najmniejszego elementu
    def smallest(self):
        if (self.left == None):
            return self.value
        else:
            return self.left.smallest()

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


# usuwanie wezla
def delete(root, node, value):
    if node.value == value: # jesli znajdziesz wezel ktory masz usunac
        # przypadek, gdy jest lisciem
        #print("odwiedzony wezel")
        #print(node.value)
        if node.left == None and node.right == None:
            del node
            return None
        # przypadek gdy ma prawe dziecko
        elif node.left == None and node.right != None:
            return node.right  #zwroc prawe dziecko na jego miejsce
        # przypadek gdy ma lewe dziecko
        elif node.right == None and node.left != None:
            return node.left # zwroc lewe dziecko na jego miejsce
        else:
            # zmienna pomocnicza wskazujaca na pierwsze prawe dziecko
            change = node.right
            while change.left != None:  # dopoki prawe dziecko ma lewe dziecko
                change = change.left  # idz w lewo
            node.value = change.value  # zamien warosc maksymalnego lewego dziecka z wartoscia wezla do usuniecia
            node.right = delete(root, node.right, change.value)  # rekurencyjnie usun dziecko, z ktorego wartoscia sie zamieniles
    elif node.value > value:
        #print("odwiedzony wezel")
        #print(node.value)
        node.left = delete(root, node.left, value) #jesli wartosc szukanego wezla jest mniejsza to idz w lewo z delete
    elif node.value < value:
        #print("odwiedzony wezel")
        #print(node.value)
        node.right = delete(root, node.right, value) #jesli wartosc szukanego wezla jest wieksza to idz w prawo z delete
    return node #zwroc wezel nastepnego wyswietlenia


def deletemany(tree):
    print("Ile wezlow chcesz usunac?")
    a = input()
    a = int(a)
    for i in range(a):
        print("Podaj wartosc wezla, ktory chcesz usunac")
        nodevalue = int(input())
        delete(tree, tree, nodevalue)


# tworzenie drzewa BST
def randomBST(tab):
    BSTtree = BSTTreenode(tab[0])
    for i in tab[1:]:
        BSTtree.insertnode(i)
    return BSTtree


# Tworzenie drzewa AVL i "wrzucanie" do niego danych z tablicy metoda polowkowa
def divide(node, tab):
    if len(tab) == 1:
        node.insertnode(tab[0])
    elif len(tab) >= 2:
        mid = len(tab) // 2
        node.insertnode(tab[mid])
        divide(node, tab[:mid])
        divide(node, tab[mid+1:])


# funkcja tworzaca miejsce na drzewo AVL
def BinaryAVL(tab):
    mid = len(tab) // 2
    avltree = AVLTreenode(tab[mid])
    divide(avltree, tab[:mid])
    divide(avltree, tab[mid + 1:])
    return avltree


# Przeszukiwanie drzewa in-order
def inorder(node, path):
    if node.left != None:
        inorder(node.left,path)
    path.append(node.value)
    if node.right != None:
        inorder(node.right,path)


# Przeszukiwanie drzewa pre-order
def preorder(node, path):
    path.append(node.value)
    if node.left != None:
        preorder(node.left,path)
    if node.right != None:
        preorder(node.right,path)


def postorder(root, node, path):
    if node.left != None:
        postorder(root, node.left, path)
    if node.right != None:
        postorder(root, node.right, path)
    path.append(node.value)
    print("odwiedzony wezel")
    print(node.value)
    delete(root, root, node.value)
    if root.value == node.value:
        root.__del__()


def preorderfromuser(node, key):
    if node.value == key:
        path = []
        preorder(node, path)
        print(path)
    if node.left != None:
        preorderfromuser(node.left,key)
    if node.right != None:
        preorderfromuser(node.right,key)


# Rotacje
def RR(node):
    if node.left != None:
        B = node.left
        A = node
        node.left = node.left.right
        B.right = A
        node = B
    return node


def RL(node):
    if node.right != None:
        B = node.right
        A = node
        node.right = node.right.left
        B.left = A
        node = B
    return node


# przerabianie drzewa na liste
def makinglist(node):
    while node.left != None:
        node = RR(node)
    if node.right != None:
       node.right = makinglist(node.right)
    return node


# funckja obliczajaca ilosc potrzebnych rotacji
def canfit(n):
    y = math.floor(math.log(n + 1, 2))
    x = pow(2, y) - 1
    return x

# funkcja do rotowania drzewa okreslona ilosc razy w lewo
def leftrotations(node, n):
    if n > 0:
        #obroc w lewo korzen
        node = RL(node)
        # rekurencyjnie wywoluj dla kazdego prawego dziecka nast
        if node.right != None:
            node.right = leftrotations(node.right, n - 1)
        return node
    else:
        return node

# wywoluje rotacje w lewo odpowiednia ilosc razy
def balancingtree(root, maxnodes):
    rotations = canfit(maxnodes)
    leaves = maxnodes - rotations
    root = makinglist(root)

    # rotacje wstepne
    root = leftrotations(root, leaves)

    # rotacje ustawiajace reszte drzewa
    rotations = rotations // 2
    while(rotations > 0):
        root = leftrotations(root, rotations)
        rotations = rotations // 2
    return root


# tworzenie tablicy z losowymi wartosciami ulozonymi malejaco
def decreasingtable(elem_quan, random_range):
    decrease = 10
    border = random_range - decrease
    first = random.randint(border, random_range)
    table = [first]
    i = 0
    while len(table) < elem_quan:
        elem = random.randint(border, random_range)
        if elem <= table[i]:
            border -= decrease
            random_range -= decrease
            i += 1
            table.append(elem)
    return table


def testAVLcreation(quan):
    file = open("C:/Users/Mateusz Rzepka/Desktop/wyniki drzewa/Wyniki_AVL_creation.txt", "a")
    howmany = quan
    range = howmany * 10

    table1 = merge_sort(decreasingtable(howmany, range))
    table2 = merge_sort(decreasingtable(howmany, range))
    table3 = merge_sort(decreasingtable(howmany, range))
    table4 = merge_sort(decreasingtable(howmany, range))
    table5 = merge_sort(decreasingtable(howmany, range))
    table6 = merge_sort(decreasingtable(howmany, range))
    table7 = merge_sort(decreasingtable(howmany, range))
    table8 = merge_sort(decreasingtable(howmany, range))
    table9 = merge_sort(decreasingtable(howmany, range))
    table10 = merge_sort(decreasingtable(howmany, range))

    start = time.time()
    tree1 = BinaryAVL(table1)
    end = time.time()
    worktime1 = end - start

    start = time.time()
    tree2 = BinaryAVL(table2)
    end = time.time()
    worktime2 = end - start

    start = time.time()
    tree3 = BinaryAVL(table3)
    end = time.time()
    worktime3 = end - start

    start = time.time()
    tree4 = BinaryAVL(table4)
    end = time.time()
    worktime4 = end - start

    start = time.time()
    tree5 = BinaryAVL(table5)
    end = time.time()
    worktime5 = end - start

    start = time.time()
    tree6 = BinaryAVL(table6)
    end = time.time()
    worktime6 = end - start

    start = time.time()
    tree7 = BinaryAVL(table7)
    end = time.time()
    worktime7 = end - start

    start = time.time()
    tree8 = BinaryAVL(table8)
    end = time.time()
    worktime8 = end - start

    start = time.time()
    tree9 = BinaryAVL(table9)
    end = time.time()
    worktime9 = end - start

    start = time.time()
    tree10 = BinaryAVL(table10)
    end = time.time()
    worktime10 = end - start

    averagetime = (worktime1 + worktime2 + worktime3 + worktime4 + worktime5 + worktime6 + worktime7 + worktime8 + worktime9 + worktime10)/10

    file.write("Testy AVL")
    file.write("\n")
    file.write(str(quan))
    file.write(" elementow")
    file.write("\n")
    file.write("czas sredni: \n")
    file.write(str(averagetime))
    file.write("\n")

    file.close()


def testrandomBSTcreation(quan):
    file = open("C:/Users/Mateusz Rzepka/Desktop/wyniki drzewa/Wyniki_BST_creation.txt", "a")
    howmany = quan
    range = howmany * 10

    table1 = decreasingtable(howmany, range)
    table2 = decreasingtable(howmany, range)
    table3 = decreasingtable(howmany, range)
    table4 = decreasingtable(howmany, range)
    table5 = decreasingtable(howmany, range)
    table6 = decreasingtable(howmany, range)
    table7 = decreasingtable(howmany, range)
    table8 = decreasingtable(howmany, range)
    table9 = decreasingtable(howmany, range)
    table10 = decreasingtable(howmany, range)

    start = time.time()
    tree1 = randomBST(table1)
    end = time.time()
    worktime1 = end - start

    start = time.time()
    tree2 = randomBST(table2)
    end = time.time()
    worktime2 = end - start

    start = time.time()
    tree3 = randomBST(table3)
    end = time.time()
    worktime3 = end - start

    start = time.time()
    tree4 = randomBST(table4)
    end = time.time()
    worktime4 = end - start

    start = time.time()
    tree5 = randomBST(table5)
    end = time.time()
    worktime5 = end - start

    start = time.time()
    tree6 = randomBST(table6)
    end = time.time()
    worktime6 = end - start

    start = time.time()
    tree7 = randomBST(table7)
    end = time.time()
    worktime7 = end - start

    start = time.time()
    tree8 = randomBST(table8)
    end = time.time()
    worktime8 = end - start

    start = time.time()
    tree9 = randomBST(table9)
    end = time.time()
    worktime9 = end - start

    start = time.time()
    tree10 = randomBST(table10)
    end = time.time()
    worktime10 = end - start

    averagetime = (worktime1 + worktime2 + worktime3 + worktime4 + worktime5 + worktime6 + worktime7 + worktime8 + worktime9 + worktime10) / 10

    file.write("Testy BST")
    file.write("\n")
    file.write(str(quan))
    file.write(" elementow")
    file.write("\n")
    file.write("czas sredni: \n")
    file.write(str(averagetime))
    file.write("\n")

    file.close()


def testsmallestBST(quan):
    file = open("C:/Users/Mateusz Rzepka/Desktop/wyniki drzewa/Wyniki_BST_smallest.txt", "a")
    howmany = quan
    range = howmany * 10

    table1 = decreasingtable(howmany, range)
    table2 = decreasingtable(howmany, range)
    table3 = decreasingtable(howmany, range)
    table4 = decreasingtable(howmany, range)
    table5 = decreasingtable(howmany, range)
    table6 = decreasingtable(howmany, range)
    table7 = decreasingtable(howmany, range)
    table8 = decreasingtable(howmany, range)
    table9 = decreasingtable(howmany, range)
    table10 = decreasingtable(howmany, range)

    tree1 = randomBST(table1)
    tree2 = randomBST(table2)
    tree3 = randomBST(table3)
    tree4 = randomBST(table4)
    tree5 = randomBST(table5)
    tree6 = randomBST(table6)
    tree7 = randomBST(table7)
    tree8 = randomBST(table8)
    tree9 = randomBST(table9)
    tree10 = randomBST(table10)

    start = time.time()
    smallest1 = tree1.smallest()
    stop = time.time()
    worktime1 = stop - start

    start = time.time()
    smallest2 = tree2.smallest()
    stop = time.time()
    worktime2 = stop - start

    start = time.time()
    smallest3 = tree3.smallest()
    stop = time.time()
    worktime3 = stop - start

    start = time.time()
    smallest4 = tree4.smallest()
    stop = time.time()
    worktime4 = stop - start

    start = time.time()
    smallest5 = tree5.smallest()
    stop = time.time()
    worktime5 = stop - start

    start = time.time()
    smallest6 = tree6.smallest()
    stop = time.time()
    worktime6 = stop - start

    start = time.time()
    smallest7 = tree7.smallest()
    stop = time.time()
    worktime7 = stop - start

    start = time.time()
    smallest8 = tree8.smallest()
    stop = time.time()
    worktime8 = stop - start

    start = time.time()
    smallest9 = tree9.smallest()
    stop = time.time()
    worktime9 = stop - start

    start = time.time()
    smallest10 = tree10.smallest()
    stop = time.time()
    worktime10 = stop - start

    averagetime = (worktime1 + worktime2 + worktime3 + worktime4 + worktime5 + worktime6 + worktime7 + worktime8 + worktime9 + worktime10) / 10

    file.write("Testy smallest BST")
    file.write("\n")
    file.write(str(quan))
    file.write(" elementow")
    file.write("\n")
    file.write("czas sredni: \n")
    file.write(str(averagetime))
    file.write("\n")

    file.close()


def testsmallestAVL(quan):
    file = open("C:/Users/Mateusz Rzepka/Desktop/wyniki drzewa/Wyniki_AVL_smallest.txt", "a")
    howmany = quan
    range = howmany * 10

    table1 = merge_sort(decreasingtable(howmany, range))
    table2 = merge_sort(decreasingtable(howmany, range))
    table3 = merge_sort(decreasingtable(howmany, range))
    table4 = merge_sort(decreasingtable(howmany, range))
    table5 = merge_sort(decreasingtable(howmany, range))
    table6 = merge_sort(decreasingtable(howmany, range))
    table7 = merge_sort(decreasingtable(howmany, range))
    table8 = merge_sort(decreasingtable(howmany, range))
    table9 = merge_sort(decreasingtable(howmany, range))
    table10 = merge_sort(decreasingtable(howmany, range))

    tree1 = BinaryAVL(table1)
    tree2 = BinaryAVL(table2)
    tree3 = BinaryAVL(table3)
    tree4 = BinaryAVL(table4)
    tree5 = BinaryAVL(table5)
    tree6 = BinaryAVL(table6)
    tree7 = BinaryAVL(table7)
    tree8 = BinaryAVL(table8)
    tree9 = BinaryAVL(table9)
    tree10 = BinaryAVL(table10)

    start = time.time()
    smallest1 = tree1.smallest()
    stop = time.time()
    worktime1 = stop - start

    start = time.time()
    smallest2 = tree2.smallest()
    stop = time.time()
    worktime2 = stop - start

    start = time.time()
    smallest3 = tree3.smallest()
    stop = time.time()
    worktime3 = stop - start

    start = time.time()
    smallest4 = tree4.smallest()
    stop = time.time()
    worktime4 = stop - start

    start = time.time()
    smallest5 = tree5.smallest()
    stop = time.time()
    worktime5 = stop - start

    start = time.time()
    smallest6 = tree6.smallest()
    stop = time.time()
    worktime6 = stop - start

    start = time.time()
    smallest7 = tree7.smallest()
    stop = time.time()
    worktime7 = stop - start

    start = time.time()
    smallest8 = tree8.smallest()
    stop = time.time()
    worktime8 = stop - start

    start = time.time()
    smallest9 = tree9.smallest()
    stop = time.time()
    worktime9 = stop - start

    start = time.time()
    smallest10 = tree10.smallest()
    stop = time.time()
    worktime10 = stop - start

    averagetime = (worktime1 + worktime2 + worktime3 + worktime4 + worktime5 + worktime6 + worktime7 + worktime8 + worktime9 + worktime10) / 10

    file.write("Testy smallest AVL")
    file.write("\n")
    file.write(str(quan))
    file.write(" elementow")
    file.write("\n")
    file.write("czas sredni: \n")
    file.write(str(averagetime))
    file.write("\n")

    file.close()


def inorderBST(quan):
    file = open("C:/Users/Mateusz Rzepka/Desktop/wyniki drzewa/Wyniki_BST_inorder.txt", "a")
    howmany = quan
    range = howmany * 10

    table1 = decreasingtable(howmany, range)
    table2 = decreasingtable(howmany, range)
    table3 = decreasingtable(howmany, range)
    table4 = decreasingtable(howmany, range)
    table5 = decreasingtable(howmany, range)
    table6 = decreasingtable(howmany, range)
    table7 = decreasingtable(howmany, range)
    table8 = decreasingtable(howmany, range)
    table9 = decreasingtable(howmany, range)
    table10 = decreasingtable(howmany, range)

    tree1 = randomBST(table1)
    tree2 = randomBST(table2)
    tree3 = randomBST(table3)
    tree4 = randomBST(table4)
    tree5 = randomBST(table5)
    tree6 = randomBST(table6)
    tree7 = randomBST(table7)
    tree8 = randomBST(table8)
    tree9 = randomBST(table9)
    tree10 = randomBST(table10)

    path = []
    start = time.time()
    inorder(tree1, path)
    end = time.time()
    worktime1 = end - start

    path = []
    start = time.time()
    inorder(tree2, path)
    end = time.time()
    worktime2 = end - start

    path = []
    start = time.time()
    inorder(tree3, path)
    end = time.time()
    worktime3 = end - start

    path = []
    start = time.time()
    inorder(tree4, path)
    end = time.time()
    worktime4 = end - start

    path = []
    start = time.time()
    inorder(tree5, path)
    end = time.time()
    worktime5 = end - start

    path = []
    start = time.time()
    inorder(tree6, path)
    end = time.time()
    worktime6 = end - start

    path = []
    start = time.time()
    inorder(tree7, path)
    end = time.time()
    worktime7 = end - start

    path = []
    start = time.time()
    inorder(tree8, path)
    end = time.time()
    worktime8 = end - start

    path = []
    start = time.time()
    inorder(tree9, path)
    end = time.time()
    worktime9 = end - start

    path = []
    start = time.time()
    inorder(tree10, path)
    end = time.time()
    worktime10 = end - start

    averagetime = (worktime1 + worktime2 + worktime3 + worktime4 + worktime5 + worktime6 + worktime7 + worktime8 + worktime9 + worktime10) / 10

    file.write("Testy inorder BST")
    file.write("\n")
    file.write(str(quan))
    file.write(" elementow")
    file.write("\n")
    file.write("czas sredni: \n")
    file.write(str(averagetime))
    file.write("\n")

    file.close()


def inorderAVL(quan):
    file = open("C:/Users/Mateusz Rzepka/Desktop/wyniki drzewa/Wyniki_AVL_inorder.txt", "a")
    howmany = quan
    range = howmany * 10

    table1 = merge_sort(decreasingtable(howmany, range))
    table2 = merge_sort(decreasingtable(howmany, range))
    table3 = merge_sort(decreasingtable(howmany, range))
    table4 = merge_sort(decreasingtable(howmany, range))
    table5 = merge_sort(decreasingtable(howmany, range))
    table6 = merge_sort(decreasingtable(howmany, range))
    table7 = merge_sort(decreasingtable(howmany, range))
    table8 = merge_sort(decreasingtable(howmany, range))
    table9 = merge_sort(decreasingtable(howmany, range))
    table10 = merge_sort(decreasingtable(howmany, range))

    tree1 = BinaryAVL(table1)
    tree2 = BinaryAVL(table2)
    tree3 = BinaryAVL(table3)
    tree4 = BinaryAVL(table4)
    tree5 = BinaryAVL(table5)
    tree6 = BinaryAVL(table6)
    tree7 = BinaryAVL(table7)
    tree8 = BinaryAVL(table8)
    tree9 = BinaryAVL(table9)
    tree10 = BinaryAVL(table10)

    path = []
    start = time.time()
    inorder(tree1, path)
    end = time.time()
    worktime1 = end - start

    path = []
    start = time.time()
    inorder(tree2, path)
    end = time.time()
    worktime2 = end - start

    path = []
    start = time.time()
    inorder(tree3, path)
    end = time.time()
    worktime3 = end - start

    path = []
    start = time.time()
    inorder(tree4, path)
    end = time.time()
    worktime4 = end - start

    path = []
    start = time.time()
    inorder(tree5, path)
    end = time.time()
    worktime5 = end - start

    path = []
    start = time.time()
    inorder(tree6, path)
    end = time.time()
    worktime6 = end - start

    path = []
    start = time.time()
    inorder(tree7, path)
    end = time.time()
    worktime7 = end - start

    path = []
    start = time.time()
    inorder(tree8, path)
    end = time.time()
    worktime8 = end - start

    path = []
    start = time.time()
    inorder(tree9, path)
    end = time.time()
    worktime9 = end - start

    path = []
    start = time.time()
    inorder(tree10, path)
    end = time.time()
    worktime10 = end - start

    averagetime = (worktime1 + worktime2 + worktime3 + worktime4 + worktime5 + worktime6 + worktime7 + worktime8 + worktime9 + worktime10) / 10

    file.write("Testy inorder AVL")
    file.write("\n")
    file.write(str(quan))
    file.write(" elementow")
    file.write("\n")
    file.write("czas sredni: \n")
    file.write(str(averagetime))
    file.write("\n")

    file.close()


def balancingBST(quan):
    file = open("C:/Users/Mateusz Rzepka/Desktop/wyniki drzewa/Wyniki_BST_Balancing.txt", "a")
    howmany = quan
    range = howmany * 10
    maxnodes = quan
    rotations = canfit(maxnodes)
    leaves = maxnodes - rotations

    table1 = decreasingtable(howmany, range)
    table2 = decreasingtable(howmany, range)
    table3 = decreasingtable(howmany, range)
    table4 = decreasingtable(howmany, range)
    table5 = decreasingtable(howmany, range)
    table6 = decreasingtable(howmany, range)
    table7 = decreasingtable(howmany, range)
    table8 = decreasingtable(howmany, range)
    table9 = decreasingtable(howmany, range)
    table10 = decreasingtable(howmany, range)

    tree1 = randomBST(table1)
    tree2 = randomBST(table2)
    tree3 = randomBST(table3)
    tree4 = randomBST(table4)
    tree5 = randomBST(table5)
    tree6 = randomBST(table6)
    tree7 = randomBST(table7)
    tree8 = randomBST(table8)
    tree9 = randomBST(table9)
    tree10 = randomBST(table10)

    start = time.time()
    tree1 = balancingtree(tree1, maxnodes)
    end = time.time()
    worktime1 = end - start

    start = time.time()
    tree2 = balancingtree(tree2, maxnodes)
    end = time.time()
    worktime2 = end - start

    start = time.time()
    tree3 = balancingtree(tree3, maxnodes)
    end = time.time()
    worktime3 = end - start

    start = time.time()
    tree4 = balancingtree(tree4, maxnodes)
    end = time.time()
    worktime4 = end - start

    start = time.time()
    tree5 = balancingtree(tree5, maxnodes)
    end = time.time()
    worktime5 = end - start

    start = time.time()
    tree6 = balancingtree(tree6, maxnodes)
    end = time.time()
    worktime6 = end - start

    start = time.time()
    tree7 = balancingtree(tree7, maxnodes)
    end = time.time()
    worktime7 = end - start

    start = time.time()
    tree8 = balancingtree(tree8, maxnodes)
    end = time.time()
    worktime8 = end - start

    start = time.time()
    tree9 = balancingtree(tree9, maxnodes)
    end = time.time()
    worktime9 = end - start

    start = time.time()
    tree10 = balancingtree(tree10, maxnodes)
    end = time.time()
    worktime10 = end - start

    averagetime = (worktime1 + worktime2 + worktime3 + worktime4 + worktime5 + worktime6 + worktime7 + worktime8 + worktime9 + worktime10) / 10

    file.write("Testy balancing BST")
    file.write("\n")
    file.write(str(quan))
    file.write(" elementow")
    file.write("\n")
    file.write("czas sredni: \n")
    file.write(str(averagetime))
    file.write("\n")

    file.close()

