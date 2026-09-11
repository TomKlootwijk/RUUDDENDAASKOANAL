; Tom Klootwijk Gambit 4.0 -- edge_conservation
(set-option :produce-proofs true)
(set-option :timeout 15000)
(declare-const u Int)(declare-const v Int)(declare-const j Int)(declare-const k Int)
(assert (not (= (+ (+ (- u j) k) (+ (- v k) j)) (+ u v))))
(check-sat)
(get-proof)
