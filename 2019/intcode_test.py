import intcode

def test_02():
    pc = intcode.Computer([1,0,0,0,99])
    pc.run()
    assert pc.data.toList() == [2,0,0,0,99]
    pc.reset(vals=[2,3,0,3,99]), pc.run()
    assert pc.data.toList() == [2,3,0,6,99]
    pc.reset(vals=[2,4,4,5,99,0]), pc.run()
    assert pc.data.toList() == [2,4,4,5,99,9801]
    pc.reset(vals=[1,1,1,4,99,5,6,0,99]), pc.run()
    assert pc.data.toList() == [30,1,1,4,2,5,6,0,99]

def test_05():
    pc = intcode.Computer([1,0,0,0,99])
    pc.run()
    assert pc.data[0] == 2
    pc.reset(vals=[1,1,1,4,99,5,6,0,99]), pc.run()
    assert pc.data[0] == 30
    pc.reset(vals=[3,0,4,0,99], input=42), pc.run()
    assert pc.data[0] == 42
    pc.reset(vals=[1101,100,-1,4,0]), pc.run()
    assert pc.data.toList() == [1101,100,-1,4,99]
    pc.reset(vals=[3,9,8,9,10,9,4,9,99,-1,8]), pc.run()
    assert pc.data[0] == 0
    pc.reset(input=8), pc.run()
    assert pc.data[0] == 1
    pc.reset(vals=[3,9,7,9,10,9,4,9,99,-1,8], input=0), pc.run()
    assert pc.data[0] == 1
    pc.reset(input=8), pc.run()
    assert pc.data[0] == 0
    pc.reset(vals=[3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]), pc.run()
    assert pc.data[0] == 0
    pc.reset(input=1), pc.run()
    assert pc.data[0] == 1
    pc.reset(vals=[3,3,1105,-1,9,1101,0,0,12,4,12,99,1]), pc.run()
    assert pc.data[0] == 0
    pc.reset(input=1), pc.run()
    assert pc.data[0] == 1
    pc.reset(vals=[3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
        1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,
        1101,1000,1,20,4,20,1105,1,46,98,99]), pc.run()
    assert pc.data[0] == 999
    pc.reset(input=8), pc.run()
    assert pc.data[0] == 1000
    pc.reset(input=9), pc.run()
    assert pc.data[0] == 1001

def test_09():
    pc = intcode.Computer([104,1125899906842624,99])
    pc.run()
    assert pc.data[0] == 1125899906842624
    pc.reset(vals=[1102,34915192,34915192,7,4,7,99,0]), pc.run()
    assert len(str(pc.data[0])) == 16

if __name__ == "__main__":
    test_02()
    test_05()
    test_09()