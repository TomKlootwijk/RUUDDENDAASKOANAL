; Tom Klootwijk Gambit 4.0 -- four_edge_outflow
(set-option :produce-proofs true)
(set-option :timeout 15000)
(declare-const m Int)(declare-const a Int)(declare-const b Int)(declare-const c Int)(declare-const d Int)
(assert (and (>= m 0) (>= a 0) (>= b 0) (>= c 0) (>= d 0) (<= (* 8 a) m) (<= (* 8 b) m) (<= (* 8 c) m) (<= (* 8 d) m)))
(assert (< (- m (+ a b c d)) 0))
(check-sat)
(get-proof)
