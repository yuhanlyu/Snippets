File.open(ARGV[0]) do |f|
    n, words = f.readline.to_i
    f.readlines.map(&:chomp).sort_by(&:size)[-n..-1].reverse.map(&method(:puts))
end
