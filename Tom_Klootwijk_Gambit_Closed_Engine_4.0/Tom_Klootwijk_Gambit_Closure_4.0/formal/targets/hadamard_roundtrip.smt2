; Tom Klootwijk Gambit 4.0 -- hadamard_roundtrip
(set-option :produce-proofs true)
(set-option :timeout 15000)
(declare-const a Real)(declare-const b Real)
(define-fun c () Real (+ a b))(define-fun d () Real (- a b))
(assert (not (and (= (+ c d) (* 2 a)) (= (- c d) (* 2 b)))))
(check-sat)
(get-proof)
