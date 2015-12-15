SIZE = 256
board = Array.new(SIZE) { Array.new(SIZE, 0) }
File.open(ARGV[0]).each_line do |line|
    args = line.split(' ')
    case args[0]
    when 'SetCol'
        (0...SIZE).each { |i| board[i][args[1].to_i] = args[2].to_i }
    when 'SetRow'
        (0...SIZE).each { |i| board[args[1].to_i][i] = args[2].to_i }
    when 'QueryCol'
        puts (0...SIZE).inject(0) { |sum, i| sum + board[i][args[1].to_i] }
    when 'QueryRow'
        puts board[args[1].to_i].inject(:+)
    end
end
