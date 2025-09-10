SELECT Distinct
  p.objid,
  p.ra,
  p.dec,
  s.ra,
  s.dec,
  p.l,
  p.b,
  s.specObjID,
  s.plate,
  s.mjd,
  s.fiberid,
  s.programname,
  s.class,
  s.sdssPrimary,
  pz.*
INTO mydb.DATA7901_DR19_photoz
FROM PhotoObj AS p
  LEFT JOIN SpecObj AS s ON s.bestobjid = p.objid
  LEFT JOIN Photoz AS pz ON pz.objid = p.objid
WHERE
  p.petroMag_r BETWEEN 10.0 AND 17.7
  AND s.zWarning = 0
  AND s.z BETWEEN 0.003333 AND 0.1500000001;