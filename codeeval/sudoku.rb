File.open(ARGV[0]).each_line do |line|
    n, board = line.split(";")
    n, board = n.to_i, board.split(",").map(&:to_i).each_slice(n.to_i).to_a
    t, s = (1..n).to_a, Math.sqrt(n).to_i
    puts board.all?{|r| r.sort == t} && board.transpose.all?{|c| c.sort == t} &&
         n.times.map {|i|
             r, c = i.divmod(s)
             board[r * s, s].map {|row| row[c * s, s]}.flatten
         }.all?{|g| g.sort == t} ? "True" : "False"
end
