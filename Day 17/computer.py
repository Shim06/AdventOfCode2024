import time

def main():
    start_time = time.time()
    computer = Computer()
    instructions = []
    with open(".\\Day 17\\input.txt") as input:
        for line in input:
            instructions.append(line.removesuffix("\n"))

    for i, line in enumerate(instructions):
        if len(line) == 0:
            middle = i

    registers = instructions[0:middle]
    instructions = instructions[middle + 1:]

    temp = [0] * 3
    for i, register in enumerate(registers):
        temp[i] = register.split(":")[1]
    registers = temp

    for instruction in instructions:
        temp = instruction.split(":")[1].split(",")
    
    temp2 = [0] * len(temp)
    total = 0
    for i in range(len(temp)):
        temp2[i] = int(temp[i])
        total += temp2[i]
        
    instructions = temp2
    
    computer.a = int(registers[0])
    computer.b = int(registers[1])
    computer.c = int(registers[2])
    computer.insert_instructions(instructions)

    while computer.clock() == True:
        pass
    print(f"Output: {computer.output.removesuffix(',')}")

    execution_time = time.time() - start_time
    print(f"Execution time: {execution_time} seconds")

class Computer:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.program_counter = 0
        self.ram = []
        self.output = ""

    def clock(self):
        length = len(self.ram)
        if self.program_counter < length:
            opcode = self.ram[self.program_counter]
            operand = self.ram[self.program_counter + 1]
            self.program_counter += 2
            match opcode:
                case 0:
                    self.ADV(operand)
                    print(f"ADV {operand}")
                case 1:
                    self.BXL(operand)
                    print(f"BXL {operand}")
                case 2:
                    self.BST(operand)
                    print(f"BST {operand}")
                case 3:
                    self.JNZ(operand)
                    print(f"JNZ {operand}")
                case 4:
                    self.BXC(operand)
                    print(f"BXC {operand}")
                case 5:
                    self.OUT(operand)
                    print(f"OUT {operand}")
                case 6:
                    self.BDV(operand)
                    print(f"BDV {operand}")
                case 7:
                    self.CDV(operand)
                    print(f"CDV {operand}")
            return True
        
        return False


    def insert_instructions(self, instructions):
        self.ram = instructions


    def ADV(self, operand):
        operand = self.get_combo_operand(operand)
        self.a = self.a // (2**operand)


    def BXL(self, operand):
        self.b = self.b ^ operand

    
    def BST(self, operand):
        operand = self.get_combo_operand(operand)
        self.b = operand % 8


    def JNZ(self, operand):
        if self.a != 0:
            self.program_counter = operand


    def BXC(self, operand): # (For legacy reasons, this instruction reads an operand but ignores it.)
        self.b = self.b ^ self.c


    def OUT(self, operand):
        operand = self.get_combo_operand(operand)
        self.output += f"{operand % 8},"


    def BDV(self, operand):
        operand = self.get_combo_operand(operand)
        self.b = self.a // (2**operand)


    def CDV(self, operand):
        operand = self.get_combo_operand(operand)
        self.c = self.a // (2**operand)


    def get_combo_operand(self, operand):
        if operand == 4: operand = self.a
        elif operand == 5: operand = self.b
        elif operand == 6: operand = self.c
        return operand


if __name__ == "__main__":
    main()