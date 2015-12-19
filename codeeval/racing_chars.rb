dir, prev = '|', nil
File.open(ARGV[0]).each_line do |line|
    gate = line.index('_')
    prev, goal = prev || gate, line.index('C') || gate
    case goal <=> prev
    when -1
        dir = '/'
    when 0
        dir = '|'
    when 1
        dir = '\\'
    end
    line[goal], prev = dir, goal
    puts line
end
