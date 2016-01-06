require "set"
File.open(ARGV[0]).each_line do |line|
    nodes = line.chomp.split(",").each_with_object({}) {|w, h|
        h[w[0]]  = Hash.new{|h, k| h[k] = 0} if !h.has_key?(w[0])
        h[w[-1]] = Hash.new{|h, k| h[k] = 0} if !h.has_key?(w[-1])
        h[w[0]][w[-1]] += 1
    }
    lwc = lambda {|node|
        (nodes[node].each_pair.map {|n, count|
            if count > 0
                nodes[node][n] -= 1
                t = lwc.call(n) + 1
                nodes[node][n] += 1
            end
            t || 0
        } + [0]).max
    }
    ans = nodes.each_key.map(&lwc).max
    puts ans <= 1 ? "None" : ans
end
